"""
Domain services for the project showcase gallery.
"""

import logging
from pathlib import Path
from typing import List, Literal

from pydantic import BaseModel, Field

LOGGER = logging.getLogger(__name__)

GalleryCategory = Literal["Commercial", "Residential", "Infrastructure"]
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


class GalleryItem(BaseModel):
    """
    Gallery metadata displayed on the website.

    Attributes:
        item_id: Unique gallery item identifier.
        title: Project title.
        category: Project category used for filtering.
        image_path: Relative static image path.
        alt_text: Accessible description for the image.
    """

    item_id: int
    title: str = Field(min_length=3, max_length=120)
    category: GalleryCategory
    image_path: str
    alt_text: str = Field(min_length=5, max_length=180)


class GalleryService:
    """
    Provides read access to gallery items from local static files.
    """

    def __init__(self, gallery_directory: str) -> None:
        """
        Initialize gallery service.

        Args:
            gallery_directory: Path to gallery image files.
        """

        self._gallery_directory = Path(gallery_directory)

    def list_items(self, category: GalleryCategory | None = None) -> List[GalleryItem]:
        """
        Return gallery items, optionally filtered by category.

        Args:
            category: Optional category to filter by.

        Returns:
            Filtered or full gallery item list.
        """

        LOGGER.info("Loading gallery images from %s", self._gallery_directory)
        items = self._discover_items()
        if category is None:
            return items
        return [item for item in items if item.category == category]

    def _discover_items(self) -> List[GalleryItem]:
        """
        Build gallery item metadata from image filenames.

        Returns:
            List of gallery items discovered from files.
        """

        if not self._gallery_directory.exists():
            LOGGER.warning(
                "Gallery directory does not exist: %s", self._gallery_directory
            )
            return []

        image_files = [
            path
            for path in sorted(self._gallery_directory.iterdir())
            if path.suffix.lower() in SUPPORTED_EXTENSIONS
        ]
        discovered: List[GalleryItem] = []
        for index, image_path in enumerate(image_files, start=1):
            category = self._infer_category(name=image_path.stem)
            title = image_path.stem.replace("_", " ").replace("-", " ").title()
            discovered.append(
                GalleryItem(
                    item_id=index,
                    title=title,
                    category=category,
                    image_path=f"static/images/gallery/{image_path.name}",
                    alt_text=f"{category} project photo for {title}",
                )
            )

        LOGGER.info("Discovered %s gallery images", len(discovered))
        return discovered

    def _infer_category(self, name: str) -> GalleryCategory:
        """
        Infer category from filename.

        Args:
            name: Image filename stem.

        Returns:
            Matched gallery category.
        """

        normalized_name = name.lower()
        if "infra" in normalized_name or "bridge" in normalized_name:
            return "Infrastructure"
        if "res" in normalized_name or "home" in normalized_name:
            return "Residential"
        return "Commercial"
