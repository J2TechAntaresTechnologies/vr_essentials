# WebXR — Visión General

## Qué es WebXR
- API estándar del W3C (Immersive Web WG) para experiencias inmersivas (VR) y espaciales (AR) en navegadores.
- Expone sesiones `immersive-vr` y `immersive-ar` con seguimiento 6DoF, controladores/manos, render 3D y háptica.
- Implementado en navegadores basados en Chromium en visores (Meta Quest, Pico, etc.) y en navegadores de escritorio con visores conectados.

## Capacidades
- Render inmersivo: estereoscopía, frame loop XR de baja latencia, proyección por ojo.
- Entrada XR: controladores, perfiles de entrada estándar, hand tracking (joints) donde esté disponible.
- Módulos: Hit Test (colocar objetos), Anchors, Layers, DOM Overlay, Depth Sensing, Light Estimation (según navegador).
- Integración web nativa: WebGL/WebGPU, WebAudio, WebRTC, WebSockets, fetch/REST; despliegue por HTTPS.

## Posibilidades
- Gemelos digitales y visualización industrial en tiempo real.
- Formación/SOPs 3D, mantenimiento asistido, layout con hit‑test/anchors.
- Colaboración multiusuario (WebRTC/WS): avatares, pizarras y anotaciones.
- Demos comerciales y museografía accesibles por URL, sin instalar apps.

## Costes
- Licencias: sin coste por la API o navegador.
- Desarrollo: frontend 3D + backend, contenidos 3D (modelado/optimización).
- Infraestructura: hosting estático/HTTPS, backend (CPU/mem/red), certificados TLS (Let’s Encrypt o internos con mkcert).
- Dispositivos: visores (Quest/Pico) y Wi‑Fi 6/6E; opcional MDM para flotas.
- QA/rendimiento: LODs, glTF + Draco/Basis, budget de drawcalls y texturas.

## Comunidad
- Estandarización abierta en W3C Immersive Web (issues y PRs públicos).
- Amplio ecosistema web 3D: Three.js, Babylon.js, A‑Frame, PlayCanvas, Godot (plugin WebXR).

## Homólogos/alternativas abiertas
- OpenXR (nativo, Khronos) para C++/C#/Rust cuando se requiera acceso de bajo nivel/UX nativa.
- Monado (Linux, FOSS) como runtime OpenXR.
- Motores web abiertos con soporte XR: Three.js (MIT), Babylon.js (Apache‑2.0), A‑Frame (MIT), PlayCanvas (MIT), Godot (plugin WebXR).

## Repositorios clave
- Especificación WebXR: https://www.w3.org/TR/webxr/
- Borrador/Issues: https://github.com/immersive-web/webxr
- Organización Immersive Web: https://github.com/immersive-web
- Samples oficiales: https://github.com/immersive-web/webxr-samples
- Perfiles de entrada: https://github.com/immersive-web/webxr-input-profiles
- Three.js: https://github.com/mrdoob/three.js
- Babylon.js: https://github.com/BabylonJS/Babylon.js
- A‑Frame: https://github.com/aframevr/aframe
- PlayCanvas: https://github.com/playcanvas/engine
- Godot WebXR plugin: https://github.com/GodotVR/godot-webxr
- Wolvic (navegador XR): https://github.com/Igalia/wolvic

## Buenas prácticas
- HTTPS siempre; contexto seguro habilita funciones XR y sensores.
- Optimiza glTF/GLB: geometría (Draco), texturas (Basis/ETC1S/UASTC), LODs.
- Reutiliza materiales y texturas; limita drawcalls.
- Presupuesta GPU/CPU por visor (resolución/Hz); mide con herramientas del navegador.

## Probarlo con este repositorio
- Backend: `vrmeta_app` expone un servidor FastAPI + WebSocket y sirve un cliente WebXR de ejemplo.
- Pasos mínimos:
  - `cd vrmeta_app && pip install -e .`
  - `vrmeta-server --host 0.0.0.0 --port 8000 --reload`
  - Desde el visor, abrir `http://<IP-PC>:8000/web/index.html` (o usar HTTPS como en el README).
- El cliente de ejemplo usa Three.js y un WebSocket hacia `/ws` para intercambio básico de mensajes.
- Para un recorrido guiado, ver `docs/tutorial_webxr_vrmeta.md`.
