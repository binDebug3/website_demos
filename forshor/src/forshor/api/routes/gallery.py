"""
Gallery data routes.
"""

from typing import List

from fastapi import APIRouter, Depends, Query

from forshor.api.dependencies import get_gallery_service
from forshor.domain.gallery_service import GalleryCategory, GalleryItem, GalleryService

router = APIRouter(prefix="/api/gallery", tags=["gallery"])


@router.get("", response_model=List[GalleryItem])
def list_gallery(
    category: GalleryCategory | None = Query(default=None),
    gallery_service: GalleryService = Depends(get_gallery_service),
) -> List[GalleryItem]:
    """
    Return gallery items, optionally filtered by category.

    Args:
        category: Optional category filter.
        gallery_service: Domain service for gallery operations.

    Returns:
        Matching gallery items.
    """

    return gallery_service.list_items(category=category)
