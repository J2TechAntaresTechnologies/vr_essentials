from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from .routes import router, include_ws


def create_app() -> FastAPI:
    app = FastAPI(title="VRMeta Server", version="0.1.0")

    # API + WebSocket routes
    app.include_router(router)
    include_ws(app)

    # Static web client for WebXR testing
    app.mount("/web", StaticFiles(directory=str(_WEB_DIR)), name="web")

    @app.get("/", response_class=HTMLResponse)
    def index():
        # Serve the landing page which links to /web
        return ("""
<!doctype html>
<html>
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>VRMeta Server</title>
    <style>
      body { font-family: system-ui, sans-serif; margin: 2rem; }
      code { background: #f5f5f5; padding: 2px 6px; border-radius: 4px; }
    </style>
  </head>
  <body>
    <h1>VRMeta Server</h1>
    <p>Servidor activo. Cliente WebXR de prueba: <a href=\"/web/index.html\">/web/index.html</a></p>
    <p>Ping API: <a href=\"/api/ping\">/api/ping</a></p>
    <p>WebSocket: <code>/ws</code></p>
  </body>
</html>
        """)

    return app


# Resolve web dir lazily so packaging paths work
def _resolve_web_dir():
    import pathlib

    here = pathlib.Path(__file__).resolve()
    base = here.parent.parent  # .../src/vrmeta_server
    web = base / "vrmeta_server" / "web"
    return web


_WEB_DIR = _resolve_web_dir()
