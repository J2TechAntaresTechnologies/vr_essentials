# Índice de Manuales y Documentación del Proyecto

Este índice resume la documentación existente en el repositorio, indicando ubicación (ruta), título y función principal de cada manual o guía.

## Documentación principal

- Ruta: `vrmeta_app/README.md`
  - Título: VRMeta Server (Python + WebXR)
  - Función: Guía principal del proyecto. Explica objetivo, requisitos, instalación, ejecución del servidor (`vrmeta-server`), uso de HTTPS con Uvicorn y el cliente de prueba WebXR. Incluye un informe introductorio sobre capacidades y posibilidades de la VR.

- Ruta: `vrmeta_app/ESTADO_PROYECTO_2024-10-13.md`
  - Título: Barrido del proyecto VRMeta Server — 2024-10-13
  - Función: Snapshot del estado del proyecto. Detalla la estructura de carpetas/archivos, componentes del backend (FastAPI + WebSocket), cliente WebXR y próximos pasos sugeridos.

## Guías prácticas / tutoriales

- Ruta: `docs/tutorial_webxr_vrmeta.md`
  - Título: Tutorial paso a paso: de cero a WebXR con VRMeta
  - Función: Recorrido práctico para instalar, ejecutar por HTTP/HTTPS, entender y modificar el cliente WebXR, enviar eventos por WebSocket y sentar bases para integrar telemetría (MQTT/OPC‑UA).

## Documentación de soporte / informes

- Ruta: `docs/piloto_industria4.md`
  - Título: Plan de piloto VR para Automatización Industrial (Industria 4.0)
  - Función: Guía práctica para ejecutar 1–2 pilotos VR/MR en 8–10 semanas. Define objetivos, KPIs, integraciones (MQTT/OPC‑UA), arquitectura recomendada, seguridad, plan de trabajo, roles y riesgos.

- Ruta: `docs/vr_informe_slides.md`
  - Título: Informe VR (base: Meta Quest 3)
  - Función: Contenido en formato Markdown para diapositivas sobre estado del arte de VR/MR, hardware, runtimes, desarrollo, sectores, limitaciones y oportunidades, con conexión directa al enfoque del repositorio (Python + WebXR).

- Ruta: `docs/vr_informe_slides.html`
  - Título: Informe VR (Meta Quest 3)
  - Función: Diapositivas renderizadas con Reveal.js a partir del Markdown. Útil para presentaciones ejecutivas; usa `docs/slides.css` y recursos en `docs/assets/`.

## Recursos asociados

- Ruta: `docs/slides.css`
  - Título: Estilos para diapositivas
  - Función: Hoja de estilos para la presentación Reveal.js.

- Ruta: `docs/assets/`
  - Título: Recursos de presentación
  - Función: Imágenes y SVGs utilizados por las diapositivas.

## Notas

- El cliente de prueba WebXR servido por el backend está en `vrmeta_app/src/vrmeta_server/web/index.html` (no es un manual, pero es relevante para validar el flujo).
- Si se añaden nuevos manuales o guías, por favor actualice este índice para mantener la trazabilidad.

## Guías tecnológicas

- Ruta: `docs/webxr_overview.md`
  - Título: WebXR — Visión General
  - Función: Introducción a WebXR (qué es, capacidades, posibilidades, costes, comunidad), alternativas abiertas y enlaces a repositorios clave.

- Ruta: `docs/monado_overview.md`
  - Título: Monado — Visión General (OpenXR Runtime FOSS para Linux)
  - Función: Descripción del runtime Monado (qué es, capacidades, posibilidades, costes, comunidad), alternativas y repositorios clave para desarrollo nativo OpenXR en Linux.
