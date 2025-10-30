VRMeta Server (Python + WebXR)
==============================

Objetivo
--------

Backend Python (FastAPI + WebSocket) para conectar aplicaciones VR por WiFi usando un cliente WebXR (por ejemplo, Quest/Pico desde el navegador). Ideal para integraciones industriales (MQTT/OPC‑UA/ROS2) dejando el runtime VR al navegador del visor.

Por qué WebXR + Python
----------------------

- Compatibilidad amplia: visores standalone (Quest/Pico) soportan WebXR nativamente vía WiFi.
- Linux‑friendly: evita dependencias de SteamVR; funciona en Ubuntu 22.04 sin drivers específicos.
- Backend Python: integra fácil con MQTT, OPC‑UA, ROS2, gRPC, etc.

Requisitos
----------

- Ubuntu 22.04 con Python 3.10+
- Un visor con navegador WebXR (Meta Quest, Pico, etc.) en la MISMA red WiFi

Documentación
-------------

- Índice general: `../DOCUMENTACION_INDICE.md`
- WebXR — visión general: `../docs/webxr_overview.md`
- Monado (OpenXR, Linux) — visión general: `../docs/monado_overview.md`
- Tutorial paso a paso (recomendado): `../docs/tutorial_webxr_vrmeta.md`

Instalación
-----------

1) Activar tu venv y desde la carpeta `vrmeta_app/` instalar en editable:

```
pip install -e .
```

2) Ejecutar el servidor:

```
vrmeta-server --host 0.0.0.0 --port 8000 --reload
```
3) Desde el navegador del visor, abrir:

```
http://<IP-DE-TU-PC>:8000/
```

Luego entra a `/web/index.html` y pulsa "Enter VR". Verás un cubo girando; el cliente envía frames por WebSocket al backend.

HTTPS (opcional, puerto 8443)
----------------------------

Si quieres servir el backend en `https://` usando el puerto 8443, ejecuta Uvicorn con los certificados suministrados:

```
uvicorn --app-dir src vrmeta_server.app:create_app \
  --factory \
  --host 0.0.0.0 \
  --port 8443 \
  --ssl-certfile cert.pem \
  --ssl-keyfile key.pem
```

- El flag `--app-dir src` asegura que se cargue la copia de código localizada en `src/` (incluye `/web`).
- Puedes sustituir `cert.pem` y `key.pem` por tus propios certificados.
- Los navegadores WebXR bloquean WebXR si el certificado no es de confianza: instala un certificado válido (por ejemplo con `mkcert` + importar la CA en el visor) o usa un proxy HTTPS con certificados emitidos por una CA reconocida.

Endpoints
---------

- HTTP: `/` (landing), `/api/ping`
- WS: `/ws` (eco + broadcast básico entre clientes)

Siguientes pasos industriales
-----------------------------

- MQTT: `pip install 'vrmeta-server[mqtt]'` y publicar/consumir tópicos desde el WS (puente bidireccional)
- OPC‑UA: `pip install 'vrmeta-server[opcua]'` para leer/escribir nodos en PLCs
- ROS2 (Humble): usar `rclpy` para exponer tópicos/servicios al cliente WebXR

Ruta nativa OpenXR (opcional, avanzada)
---------------------------------------

Si necesitas nativo en Linux: instala el runtime Monado y usa OpenXR. En Python los bindings son limitados; para producción suele ser mejor usar C++ o un motor (Unity/Unreal). Este repo prioriza WebXR por simplicidad y portabilidad.

Notas
-----

- El servidor escucha en todas las interfaces (`0.0.0.0`) para acceso por WiFi.
- Si usas HTTPS/proxy, el cliente negocia `ws://`/`wss://` automáticamente.


Cliente WebXR de prueba
-----------------------

- URL: `https://<IP-DE-TU-PC>:8443/web/index.html`
- Demo basada en Three.js con un cubo turquesa rotando sobre una cuadrícula.
- Incluye chequeos básicos de WebXR (contexto HTTPS y soporte del dispositivo) y un WebSocket simple hacia el backend.
- Úsalo para validar que el visor ve el servidor (`Enter VR`) y que la conexión WebSocket funciona.

Informe: Capacidades y posibilidades de la VR (base: Meta Quest 3)
=================================================================

Resumen
-------

Este informe sintetiza el estado actual de la Realidad Virtual (VR) tomando como referencia de hardware la familia Meta Quest 3. Incluye: descripción tecnológica (gafas + controles), evolución histórica, estado del arte, componentes y sistemas operativos, ecosistema de desarrollo (lenguajes y librerías), panorama de aplicaciones por sector y un top 10 de oportunidades para integrar VR en una empresa de automatización industrial e Industria 4.0.

1) ¿Qué es la VR? (gafas + controles)
-------------------------------------

- Visualización inmersiva: un visor (HMD) con dos pantallas/una pantalla estereoscópica y ópticas que generan profundidad y un campo de visión amplio.
- Seguimiento 6DoF: posición y orientación precisas de cabeza y manos mediante cámaras y sensores inerciales (inside‑out tracking sin estaciones externas).
- Interacción: controladores con gatillos y botones, háptica, y seguimiento de manos sin mandos en muchos dispositivos.
- Seguridad y confort: límites de juego (guardian), passthrough a color para ver el entorno real y sesiones diseñadas para evitar mareo.

2) Breve evolución de la tecnología
----------------------------------

- 2012–2016: renacimiento con Oculus Rift y HTC Vive; PC VR con estaciones externas, enfoque en juegos y simulaciones.
- 2019–2021: visores standalone (Quest) integran todo en el casco; tracking inside‑out fiable; hand tracking inicial.
- 2022–2024: ópticas pancake más ligeras, passthrough a color y experiencias de realidad mixta (MR); OpenXR se consolida como estándar; hand tracking y colocalización multiusuario mejoran notablemente.
- Tendencias: renderizado foveado (donde hay eye‑tracking), compresión/streaming de baja latencia (Wi‑Fi 6/6E), mapeo de salas y anchors espaciales persistentes.

3) Estado del arte (2024+)
--------------------------

- MR de alta fidelidad: mezcla estable entre mundo real y virtual con passthrough a color y oclusión básica de objetos.
- Interacción natural: hand tracking usable para interfaces sin controladores; gestos y detección de toques.
- Estándares abiertos: OpenXR como API única entre fabricantes; WebXR para el navegador.
- Multiusuario: salas compartidas con sincronización espacial y voces integradas; avatares expresivos.
- Herramientas de productividad: diseño 3D colaborativo, revisión de gemelos digitales, tableros de datos inmersivos.

4) Componentes y hardware (enfoque: Meta Quest 3)
-------------------------------------------------

- Óptica y pantallas: lentes tipo pancake, alta resolución por ojo y tasas de refresco elevadas (90–120 Hz según modo).
- Sensores: cámaras frontales para seguimiento y passthrough a color; IMUs (giroscopio/acelerómetro); sensores de proximidad.
- Cómputo: SoC XR de última generación, GPU móvil optimizada para gráficos en tiempo real; RAM y almacenamiento integrados.
- Audio y voz: altavoces integrados de campo cercano y micrófonos para chat/voz.
- Controles: Meta Touch Plus con seguimiento 6DoF, háptica y detección de agarre; soporte de seguimiento de manos sin mandos.
- Conectividad: Wi‑Fi 6/6E para streaming/colaboración, Bluetooth para periféricos; Link/Air Link para PC VR.
- Batería y ergonomía: batería integrada con carga USB‑C; correas intercambiables y distancias interpupilares ajustables.

Ficha técnica (Meta Quest 3) — aproximada
-----------------------------------------

- Pantallas y óptica: paneles con lentes pancake; FOV amplio; passthrough a color para MR.
- Resolución por ojo: 2064 × 2208 píxeles (estereoscopía).
- Frecuencia de refresco: hasta 120 Hz (modos según app/energía).
- SoC: Qualcomm Snapdragon XR2 Gen 2 (GPU móvil optimizada XR).
- Memoria: 8 GB RAM; almacenamiento 128/512 GB (según modelo).
- Tracking: inside‑out 6DoF (cabeza/manos) + seguimiento de manos sin mandos.
- Controles: Meta Touch Plus con háptica y detección de agarre.
- Conectividad: Wi‑Fi 6/6E, Bluetooth 5.x, USB‑C; Link/Air Link para PC VR.
- Audio: altavoces integrados de campo cercano y micrófonos.
- Batería: ~2–3 horas de uso típico; carga USB‑C.
- Peso: ≈515 g (varía con correa/accesorios).
- Sistema: Meta Quest OS (Android‑based) con runtime OpenXR; navegador con WebXR.
- Gestión: modos empresariales/MDM, distribución privada (Quest for Business).

Nota: algunos valores son aproximados y pueden variar por versión de firmware, región y configuración.

5) Sistemas operativos y runtimes
---------------------------------

- Meta Quest OS: basado en Android, con runtime OpenXR y soporte para aplicaciones nativas y experiencias WebXR vía navegador.
- PC VR: compatibilidad con OpenXR (SteamVR/Oculus PC) al usar Link/Air Link; rendering en Windows y streaming al visor.
- Alternativas: Pico OS (Android), VIVE Focus (Android). Windows Mixed Reality está en retirada; visionOS (Apple) es MR con enfoque distinto.
- Gestión empresarial: MDM y “Quest for Business” para despliegues, kiosko, control de permisos y distribución privada.

6) Desarrollo: lenguajes, motores y librerías
--------------------------------------------

- Motores dominantes:
  - Unity (C#): XR Interaction Toolkit, Oculus Integration/Meta SDKs (Presence Platform: Passthrough, Scene, Hands, Anchors), soporte OpenXR.
  - Unreal Engine (C++/Blueprints): plantillas VR/MR, OpenXR, control granular de rendimiento.
  - WebXR (JS/TS): Three.js, Babylon.js, A‑Frame; ideal para acceso inmediato desde el navegador del visor.
- Nativo y otros:
  - OpenXR (C/C++): acceso de bajo nivel y máxima portabilidad. En Python y Rust existen bindings para utilidades/ tooling.
  - Godot XR (GDScript/C#): opción creciente en prototipado y proyectos abiertos.
- Redes y voz: Photon, Normcore, Vivox, WebRTC para colaboración en tiempo real.
- Integraciones industriales: MQTT, OPC‑UA, gRPC/REST; render/telemetría desde gemelos digitales (CAD/BIM/Simulaciones).
- Prácticas clave: presupuestos de frame (11 ms a 90 Hz), foveated rendering (donde aplique), batching, compresión de texturas, perfiles de energía.

7) Aplicaciones actuales por sector
-----------------------------------

- Entretenimiento y fitness: juegos inmersivos, experiencias musicales, entrenamiento físico guiado y boxeo/ritmo.
- Industria y manufactura: formación operativa segura, mantenimiento asistido, revisión de layout, validación ergonómica y SOPs 3D.
- Desarrollo e ingeniería: inspección de CAD, revisión de cambios, depuración de robots/celdas con gemelos digitales.
- Medicina y salud: educación anatómica, planificación quirúrgica, rehabilitación motora, terapias de dolor/ansiedad.
- Educación y cultura: laboratorios virtuales STEM, historia/arte inmersivos, museos y training institucional.
- AEC (arquitectura/obras): walkthrough de modelos BIM, detección temprana de colisiones, apoyo a obra.

8) Limitaciones y retos actuales
--------------------------------

- Confort y tiempos de sesión: peso/batería y fatiga visual limitan jornadas largas.
- Calidad de passthrough y oclusión: suficiente para MR interactiva, aún lejos de la visión “real‑real”.
- Eye‑tracking no universal: presente en ciertos modelos; impacta foveated y UX avanzada.
- Seguridad/IT: gestión de identidades, MDM, redes Wi‑Fi corporativas y protección de IP/PLCs.

9) Top 10 oportunidades para una empresa de automatización industrial (Industria 4.0)
-------------------------------------------------------------------------------------

1. Gemelo digital inmersivo de líneas y plantas
   - Qué: visualizar y explorar en VR el modelo 3D conectado a telemetría (SCADA/MES/PLC).
   - Beneficio: decisión más rápida, detección precoz de cuellos de botella.
   - Stack sugerido: OpenXR/WebXR + MQTT/OPC‑UA + conversión CAD/BIM.

2. Formación operacional y de seguridad basada en SOPs 3D
   - Qué: cursos VR con escenarios de riesgo y procedimientos paso a paso.
   - Beneficio: menos incidentes y menor costo de entrenamiento.
   - Stack: Unity/Unreal + LRS/LMS + cuestionarios SCORM/xAPI.

3. Mantenimiento asistido y troubleshooting remoto
   - Qué: guía en VR/MR con checklists, anotaciones y voz, integrada a órdenes de trabajo.
   - Beneficio: MTTR reducido, mayor disponibilidad.
   - Stack: WebXR + WebRTC + CMMS/EAM vía API.

4. Planificación de layout y optimización de celdas
   - Qué: reconfigurar máquinas/AGVs en VR antes de mover activos físicos.
   - Beneficio: menos retrabajo y paradas.
   - Stack: Unity + plugins CAD + datos de capacidad.

5. Programación y validación de robots en VR
   - Qué: enseñar trayectorias, zonas seguras y herramientas virtuales con colisiones.
   - Beneficio: comisionado más rápido y seguro.
   - Stack: ROS2/OPC‑UA + motores físicos + librerías de cinemática.

6. War‑room de KPIs inmersivo
   - Qué: tableros 3D con KPIs, mapas térmicos, cuellos de botella y simulaciones what‑if.
   - Beneficio: alineación cross‑funcional y foco en valor.
   - Stack: WebXR + data lake/BI + MQTT.

7. Auditorías y HAZOP virtuales
   - Qué: recorridos colaborativos con marcadores de riesgo y evidencias fotométricas.
   - Beneficio: cumplimiento ágil y trazabilidad.
   - Stack: OpenXR/WebXR + repositorio de evidencias.

8. Ventas y preventa técnica
   - Qué: demostraciones inmersivas de celdas/maquinaria a escala real.
   - Beneficio: ciclos de venta más cortos y mayor tasa de cierre.
   - Stack: WebXR (acceso sin instalación) + CDN seguro.

9. Laboratorio virtual para I+D
   - Qué: prototipado rápido de HMI/UX y pruebas con usuarios internos.
   - Beneficio: iteración rápida y menos retrabajo en planta.
   - Stack: Unity/Unreal + pipelines CI de assets.

10. Capacitación de respuesta a emergencias
   - Qué: simulaciones multiusuario de incidentes y evacuación.
   - Beneficio: reducción de tiempo de reacción y coordinación efectiva.
   - Stack: Unreal/Unity + voz integrada + analítica.

10) Conexión con este repo (rápido de probar)
---------------------------------------------

- WebXR + Python: usando este `vrmeta-server`, puedes enviar/recibir telemetría (MQTT/OPC‑UA) hacia el visor desde el navegador del Quest 3 en la misma red.
- Prototipo: renderiza UI 3D con Three.js en `web/` y consume datos del backend por WebSocket.
- Escalado: migra a OpenXR nativo cuando necesites funciones avanzadas (colisiones de alta fidelidad, físicas complejas) manteniendo OpenXR para portabilidad.

Referencias prácticas
---------------------

- Estándares: OpenXR (nativo) y WebXR (web).
- Motores: Unity/Unreal como primera elección; WebXR para acceso inmediato.
- Buenas prácticas: 90 Hz mínimo cuando sea posible, evitar UI pegada a la cara, interacción bimanual consistente, sesiones cortas con checkpoints.

Diapositivas (resumen)
----------------------

- Archivo: `docs/vr_informe_slides.md`
- Cómo verlas rápidamente:
  - Opción simple: abrir en tu IDE con “Markdown Preview” y avanzar por secciones (`---`).
  - Opción presentable: usar `reveal-md docs/vr_informe_slides.md` o `marp docs/vr_informe_slides.md -o out.html` si tienes Node/Marp instalados.
  - Compartir: exporta a PDF desde el navegador o desde Marp.

Presentación HTML lista
-----------------------

- Archivo: `docs/vr_informe_slides.html`
- Estilo y logo: `docs/slides.css`, `docs/assets/logo_placeholder.svg` (puedes reemplazar el SVG por tu logo).
- Uso: abre el HTML en un navegador; usa flechas/espacio para navegar. Imprime a PDF con “Imprimir → Guardar como PDF”.

Piloto industrial (guía)
-----------------------

- Documento: `docs/piloto_industria4.md`
- Contiene: objetivos, selección de caso, KPIs, integraciones, seguridad/MDM, plan 8–10 semanas, roles, costos, riesgos y entregables.
