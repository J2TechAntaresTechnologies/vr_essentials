# Monado — Visión General (OpenXR Runtime FOSS para Linux)

## Qué es Monado
- Runtime OpenXR de código abierto mantenido principalmente por Collabora, alojado en freedesktop.org.
- Proporciona las funciones necesarias para que aplicaciones OpenXR (C++/C#/Rust, motores como Godot/Unreal) se ejecuten en Linux.
- Integra drivers y backends para distintos HMDs/controladores y puede apoyarse en OpenHMD u otros componentes.

## Capacidades
- Cumplimiento de OpenXR: capas, espacios, acciones, vistas estereoscópicas y composición.
- Soporte de dispositivos: depende del driver (OpenHMD, cámaras, IMUs); lista actualizada en documentación de Monado.
- Herramientas: modo headless, pruebas, registros detallados; compositor propio; soporte para extensiones seleccionadas.
- Integración: funciona con motores y apps que usen el loader de OpenXR (Khronos OpenXR‑SDK) en Linux.

## Posibilidades
- Desarrollo VR nativo en Linux sin depender de runtimes propietarios.
- Investigación/robótica y entornos industriales Linux‑first.
- Integración con pipelines CI y servidores X11/Wayland; POCs de tracking y algoritmos.
- Base para proyectos educativos/laboratorio con hardware soportado.

## Costes
- Licencias: sin coste (FOSS). Posible inversión en soporte/consultoría si se requiere.
- Desarrollo: integración de OpenXR en la app/motor elegido; adaptación a dispositivos soportados.
- Hardware: visores compatibles; cámaras/sensores si aplica; GPU adecuada.
- Mantenimiento: actualizar kernel/mesa/drivers; pruebas por distro/entorno gráfico.

## Comunidad
- Abierto en GitLab (issues/MRs públicos); liderazgo de Collabora con contribuciones de la comunidad.
- Documentación y guía de desarrollo en el sitio del proyecto; debates técnicos en foros/listas de freedesktop.

## Homólogos/alternativas
- SteamVR runtime (propietario, Linux/Windows), Oculus runtime (propietario, Windows), Windows Mixed Reality (propietario, legado).
- OpenHMD (FOSS, stack de drivers para HMDs) como complemento/alternativa a drivers.
- ALVR (FOSS) para streaming VR desde PC a visores standalone; puede combinarse con apps OpenXR.
- Godot OpenXR plugin (FOSS) para motor Godot con OpenXR en Linux.

## Repositorios clave
- Monado (runtime): https://gitlab.freedesktop.org/monado/monado
- Sitio/Docs de Monado: https://monado.freedesktop.org/
- OpenXR SDK (loader/headers): https://github.com/KhronosGroup/OpenXR-SDK
- OpenHMD (drivers HMD): https://github.com/OpenHMD/OpenHMD
- Godot OpenXR plugin: https://github.com/GodotVR/godot_openxr
- ALVR (streaming): https://github.com/alvr-org/ALVR

## Consideraciones prácticas
- Verifica compatibilidad del HMD/controladores en la lista de dispositivos soportados por Monado.
- Usa el loader de OpenXR (Khronos) para seleccionar el runtime (Monado) en Linux.
- Para motores (Godot/Unreal), activa OpenXR y valida con las herramientas de Monado.
- Mide latencia y estabilidad; ajusta compositor/entorno gráfico (Wayland/X11) según resultados.

