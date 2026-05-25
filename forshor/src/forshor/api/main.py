"""
FastAPI application entrypoint.
"""

import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from forshor.api.routes.gallery import router as gallery_router
from forshor.api.routes.health import router as health_router
from forshor.api.routes.leads import router as leads_router
from forshor.api.routes.pages import router as pages_router
from forshor.config import settings

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI app.

    Returns:
        Configured FastAPI application instance.
    """

    LOGGER.info(
        "Creating %s application in %s", settings.app_name, settings.environment
    )
    app = FastAPI(title=settings.app_name, version="0.1.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.mount("/static", StaticFiles(directory=PACKAGE_ROOT / "static"), name="static")

    app.include_router(pages_router)
    app.include_router(health_router)
    app.include_router(leads_router)
    app.include_router(gallery_router)

    return app


app = create_app()
