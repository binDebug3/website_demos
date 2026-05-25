"""
Health and readiness routes.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["health"])


@router.get("/health")
def healthcheck() -> dict[str, str]:
    """
    Return basic health status.

    Returns:
        Service status payload.
    """

    return {"status": "ok"}
