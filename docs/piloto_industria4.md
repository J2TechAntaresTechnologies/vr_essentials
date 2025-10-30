# Plan de piloto VR para Automatización Industrial (Industria 4.0)

Versión: 1.0 — Enfoque práctico para ejecutar 1–2 pilotos en 8–10 semanas.

## 1) Objetivo y alcance
- Meta: validar valor de negocio con VR/MR en un caso crítico (seguridad, tiempo o costo).
- Alcance típico: 1 célula/área, 5–10 usuarios, entorno de pruebas IT controlado.

## 2) Selección del caso (elige 1)
- Gemelo digital inmersivo con telemetría (SCADA/MES/PLC).
- Formación operativa y seguridad (SOPs 3D) con evaluación.
- Mantenimiento asistido remoto con checklist y voz.
- Programación/validación de robots (trayectorias/colisiones) offline.

## 3) KPIs sugeridos
- Seguridad: incidentes, near-miss, cumplimiento de SOPs.
- Operación: MTTR, OEE, tiempos de cambio (SMED), scrap.
- Formación: tiempo a competencia, retención, errores post‑entrenamiento.
- Económicos: ROI esperado, ahorro por hora parada, costo por entrenamiento.

## 4) Datos e integraciones
- Telemetría: MQTT u OPC‑UA (lectura/escritura) con tópicos/nodos documentados.
- Modelos 3D: CAD/BIM simplificado (LOD), unidades y ejes coherentes.
- Backend: Python (FastAPI/WS) o servicios existentes (REST/gRPC).
- Identidad: SSO/usuarios de prueba; auditoría básica de eventos.

## 5) Arquitectura recomendada
- Prototipo rápido: WebXR (Three.js/A‑Frame) + WebSocket + MQTT/OPC‑UA.
- Escalado: Unity/Unreal con OpenXR cuando se requiera física/UX avanzada.
- Red: Wi‑Fi 6/6E, QoS básico, segmentación para equipos/PLCs.

## 6) Seguridad y cumplimiento
- MDM/Quest for Business: kiosk mode, control de permisos, update policies.
- Datos: anonimización cuando aplique; cifrado en tránsito (TLS); registro de acceso.
- Planta: no exponer PLCs a Internet; DMZ industrial; mínimo privilegio.

## 7) Plan de trabajo (8–10 semanas)
- Sem 0–1: definición de caso, KPIs, acceso a datos, riesgos, usuarios piloto.
- Sem 2–4: prototipo funcional (WebXR + backend + telemetría), prueba técnica.
- Sem 5–7: iteraciones UX, contenido (SOPs/modelos), pruebas con usuarios.
- Sem 8–10: validación de KPIs, hardening IT/MDM, informe y decisión de escalado.

## 8) Roles
- Product owner (negocio), líder técnico XR, IT/seguridad, experto de dominio (operaciones/mantenimiento), diseñador 3D/UX, formador.

## 9) Costos y recursos (estimativo)
- Hardware: visores y accesorios; PC si hay PC VR.
- Software: licencias (motor/colaboración), MDM.
- Integración: horas de desarrollo, conversión de modelos, QA.
- Soporte: soporte IT, seguridad, capacitación.

## 10) Riesgos y mitigación
- Ciberseguridad: segmentación/red, MDM, revisión de permisos.
- UX/confort: sesiones cortas, 90 Hz, guías ergonómicas.
- Datos: calidad del modelo CAD y mapeo de tags/nodos.
- Adopción: involucrar usuarios clave, métricas transparentes, quick wins.

## 11) Entregables
- Prototipo ejecutable (WebXR/Unity/Unreal) + backend.
- Documentación de integraciones y SOPs.
- Informe de resultados de KPIs y plan de escalado (o cierre).

