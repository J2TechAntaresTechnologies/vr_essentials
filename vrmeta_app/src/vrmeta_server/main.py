import argparse
import uvicorn

from .app import create_app


def cli():
    parser = argparse.ArgumentParser(description="VRMeta Server")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--reload", action="store_true")
    args = parser.parse_args()

    # For reload/workers, Uvicorn requires an import string or factory.
    # Use factory mode when --reload is enabled; otherwise pass the app instance.
    if args.reload:
        uvicorn.run(
            "vrmeta_server.app:create_app",
            factory=True,
            host=args.host,
            port=args.port,
            reload=True,
        )
    else:
        app = create_app()
        uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    cli()
