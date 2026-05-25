"""
Dependency container for shared services.
"""

from forshor.config import settings
from forshor.domain.gallery_service import GalleryService
from forshor.domain.lead_service import LeadService

LEAD_SERVICE = LeadService()
GALLERY_SERVICE = GalleryService(gallery_directory=settings.gallery_directory)


def get_lead_service() -> LeadService:
    """
    Return the lead service singleton.

    Returns:
        Active LeadService instance.
    """

    return LEAD_SERVICE


def get_gallery_service() -> GalleryService:
    """
    Return the gallery service singleton.

    Returns:
        Active GalleryService instance.
    """

    return GALLERY_SERVICE
