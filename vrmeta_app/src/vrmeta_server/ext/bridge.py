from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Callable, Awaitable


@dataclass
class MQTTBridge:
    host: str
    port: int = 1883
    topic_prefix: str = "vrmeta"

    _connected: bool = False

    async def start(self) -> None:
        try:
            import asyncio_mqtt  # type: ignore
        except Exception as exc:  # pragma: no cover - optional
            raise RuntimeError("Instala con extra [mqtt]") from exc
        # Implementación mínima diferida: ejemplo de conexión
        # Se completa al momento de integrar con el WS
        self._connected = True

    async def publish(self, topic: str, payload: str) -> None:
        if not self._connected:
            raise RuntimeError("MQTTBridge no conectado")
        # Placeholder: implementar con asyncio-mqtt
        return None


@dataclass
class OPCUABridge:
    endpoint: str
    _connected: bool = False

    async def start(self) -> None:
        try:
            import asyncua  # type: ignore
        except Exception as exc:  # pragma: no cover - optional
            raise RuntimeError("Instala con extra [opcua]") from exc
        self._connected = True

    async def read_node(self, node_id: str) -> Optional[str]:
        if not self._connected:
            raise RuntimeError("OPCUABridge no conectado")
        # Placeholder de lectura
        return None

