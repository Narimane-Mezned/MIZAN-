from fastapi import FastAPI

from mizan import __version__
from mizan.api.v1 import health
from mizan.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version=__version__)
    app.include_router(health.router)
    return app


app = create_app()