# Tutorial paso a paso: de cero a WebXR con VRMeta

Objetivo: en 60–90 minutos tendrás un entorno funcionando, verás una demo WebXR desde tu visor (Quest/Pico), entenderás cómo está armado el cliente WebXR, cómo hablar con el backend por WebSocket y cómo empezar a modificar la escena 3D y extender el servidor.

Requisitos previos
- Ubuntu 22.04 con Python 3.10 o superior.
- Un visor con navegador WebXR (Meta Quest, Pico, Wolvic en Android), en la misma red Wi‑Fi que tu PC.
- Conocimientos básicos de terminal y JavaScript.

1) Preparar entorno e instalar
1. Activa tu entorno virtual y entra a la carpeta del proyecto (`vrmeta_app/` contiene el paquete Python):
   - `cd vrmeta_app`
   - `pip install -e .`

2) Ejecutar el servidor
- Modo desarrollo con autoreload:
  - `vrmeta-server --host 0.0.0.0 --port 8000 --reload`
- Verifica endpoints desde tu PC:
  - `http://localhost:8000/` y `http://localhost:8000/api/ping`

3) Probar desde el visor (HTTP)
- En el navegador del visor abre: `http://<IP-DE-TU-PC>:8000/web/index.html`
- Si ves la escena 3D y el botón “Enter VR”, entra a VR y comprueba que el cubo rota.
- Nota: algunos navegadores exigen contexto seguro (HTTPS) para habilitar WebXR. Si el botón no aparece, usa el paso 4.

4) Servir por HTTPS (recomendado)
- Uvicorn con certificados locales (incluidos):
  - `uvicorn --app-dir src vrmeta_server.app:create_app --factory --host 0.0.0.0 --port 8443 --ssl-certfile cert.pem --ssl-keyfile key.pem`
- En el visor, abre: `https://<IP-DE-TU-PC>:8443/web/index.html`
- Si el certificado no es de confianza, WebXR puede bloquear el modo VR. Soluciones:
  - Generar certificados con `mkcert` y añadir la CA al visor (MDM o manualmente).
  - Usar un proxy HTTPS con certificados válidos (por ejemplo, Caddy/Traefik/NGINX) frente a Uvicorn.

5) Estructura mínima del proyecto
- Backend FastAPI + WS:
  - App: `vrmeta_app/src/vrmeta_server/app.py`
  - Rutas API/WS: `vrmeta_app/src/vrmeta_server/routes.py`
  - CLI: `vrmeta_app/src/vrmeta_server/main.py`
- Cliente WebXR (estático):
  - `vrmeta_app/src/vrmeta_server/web/index.html`

6) Entender el cliente WebXR (Three.js)
- Habilita XR: `renderer.xr.enabled = true` y añade `VRButton`.
- Bucle de render: `renderer.setAnimationLoop(...)` para 90/120 Hz.
- WebSocket a backend: `const ws = new WebSocket((wss|ws) + '/ws')`.
- Objetos básicos: escena, cámara, luces, malla (cubo) y grilla.

7) Primeras modificaciones a la escena
- Abre `vrmeta_app/src/vrmeta_server/web/index.html` en tu editor.
- Cambia el color del cubo (propiedad `color` del `MeshStandardMaterial`).
- Añade una esfera bajo el cubo:
  ```js
  const sphere = new THREE.Mesh(
    new THREE.SphereGeometry(0.6, 32, 16),
    new THREE.MeshStandardMaterial({ color: 0xffb703, roughness: 0.5 })
  );
  sphere.position.set(0.8, 0.6, -1.2);
  scene.add(sphere);
  ```
- Guarda, y si corriste con `--reload`, recarga la página en el visor.

8) Interacción con controladores (eventos XR)
- Three.js expone controladores WebXR vía `renderer.xr.getController(index)`.
- Ejemplo mínimo para “apretar gatillo” y cambiar color del cubo:
  ```js
  const controller = renderer.xr.getController(0);
  controller.addEventListener('selectstart', () => {
    cube.material.color.setHex(Math.random() * 0xffffff);
    if (ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({ type: 'select', source: 0 }));
    }
  });
  scene.add(controller);
  ```
- Tip: si quieres manos/modelos 3D de controladores, importa `XRControllerModelFactory` desde `three/examples`.

9) Mensajes en tiempo real (WebSocket)
- El cliente ya envía un mensaje `frame` por render. Puedes enviar eventos propios (como `select` arriba).
- El backend (hub simple) eco/broadcast ya está implementado: `vrmeta_app/src/vrmeta_server/routes.py`.
- Para registrar mensajes en el servidor agrega logs dentro del bucle de WS:
  - Ruta: `vrmeta_app/src/vrmeta_server/routes.py:48` (dentro de `websocket_endpoint`)
  - Ejemplo: `print('WS:', msg)`

10) Cargar modelos glTF/GLB (opcional)
- Importa loader desde unpkg:
  ```js
  import { GLTFLoader } from 'https://unpkg.com/three@0.160.0/examples/jsm/loaders/GLTFLoader.js';
  const loader = new GLTFLoader();
  loader.load('/web/models/robot.glb', (gltf) => {
    const model = gltf.scene;
    model.position.set(0, 0, -2);
    scene.add(model);
  });
  ```
- Coloca tus modelos en `vrmeta_app/src/vrmeta_server/web/models/`.

11) Telemetría/PLC: puente MQTT/OPC‑UA (avanzado)
- El módulo `ext/bridge.py` incluye esqueletos de `MQTTBridge` y `OPCUABridge`.
- Instala extras cuando sea necesario:
  - MQTT: `pip install 'vrmeta-server[mqtt]'`
  - OPC‑UA: `pip install 'vrmeta-server[opcua]'`
- Idea de integración: crear una tarea de fondo en FastAPI que escuche tópicos/nodos y publique eventos por `hub.broadcast(...)` hacia los clientes WebXR.

12) Troubleshooting rápido
- No aparece “Enter VR”: usa HTTPS con certificado confiable; verifica soporte WebXR del navegador del visor.
- Pantalla negra o stutter: baja complejidad (menos drawcalls), texturas comprimidas (Basis), limita sombras.
- No conecta WS: puertos/firewall, `wss://` detrás de proxy, misma red y sin Captive Portal.
- Certificados: usa `mkcert` y carga la CA al visor (MDM o manual) o un proxy con TLS válido.

13) Siguientes pasos
- Añadir HUD de datos (KPIs) y sincronización multiusuario (broadcast → avatares simples).
- Conectar a MQTT/OPC‑UA y mapear telemetría a materiales/animaciones.
- Extraer el cliente WebXR a un proyecto separado (Vite) si el frontend crece.

Referencias
- WebXR overview del repo: `docs/webxr_overview.md`
- Índice de documentación del repo: `DOCUMENTACION_INDICE.md`

