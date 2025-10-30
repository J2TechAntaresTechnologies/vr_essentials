import asyncio
import json
from typing import Set

from fastapi import APIRouter, WebSocket, WebSocketDisconnect


router = APIRouter(prefix="/api", tags=["api"])


@router.get("/ping")
async def ping():
    return {"ok": True}


# WebSocket lives at /ws (outside the /api prefix)
ws_router = APIRouter()


class Hub:
    def __init__(self) -> None:
        self._clients: Set[WebSocket] = set()
        self._lock = asyncio.Lock()

    async def connect(self, ws: WebSocket) -> None:
        await ws.accept()
        async with self._lock:
            self._clients.add(ws)

    async def disconnect(self, ws: WebSocket) -> None:
        async with self._lock:
            self._clients.discard(ws)

    async def broadcast(self, message: dict) -> None:
        data = json.dumps(message)
        async with self._lock:
            targets = list(self._clients)
        for ws in targets:
            try:
                await ws.send_text(data)
            except RuntimeError:
                # Likely closed
                pass


hub = Hub()


@ws_router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await hub.connect(ws)
    try:
        # Send a hello banner
        await ws.send_text(json.dumps({"type": "hello", "msg": "connected"}))
        while True:
            text = await ws.receive_text()
            try:
                msg = json.loads(text)
            except json.JSONDecodeError:
                msg = {"type": "text", "data": text}

            # Echo back and broadcast to others (very simple hub)
            await ws.send_text(json.dumps({"type": "echo", "msg": msg}))
            await hub.broadcast({"type": "broadcast", "from": id(ws), "msg": msg})
    except WebSocketDisconnect:
        await hub.disconnect(ws)


# Mount ws router at root level (added by main)
def include_ws(app):
    app.include_router(ws_router)
