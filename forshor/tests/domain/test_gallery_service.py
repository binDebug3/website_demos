"""
Domain tests for gallery service.
"""

from forshor.domain.gallery_service import GalleryService


def test_gallery_service_returns_empty_when_no_images(tmp_path) -> None:
    """
    Validate empty gallery behavior.

    Args:
        tmp_path: Temporary directory fixture.

    Returns:
        None.
    """

    service = GalleryService(gallery_directory=str(tmp_path))
    assert service.list_items() == []


def test_gallery_service_discovers_images(tmp_path) -> None:
    """
    Validate gallery item discovery from filenames.

    Args:
        tmp_path: Temporary directory fixture.

    Returns:
        None.
    """

    (tmp_path / "commercial_slab.jpg").write_bytes(b"binary")
    (tmp_path / "res_foundation.png").write_bytes(b"binary")
    (tmp_path / "bridge_deck.webp").write_bytes(b"binary")

    service = GalleryService(gallery_directory=str(tmp_path))
    items = service.list_items()

    assert len(items) == 3
    categories = {item.category for item in items}
    assert categories == {"Commercial", "Residential", "Infrastructure"}


def test_gallery_service_filters_by_category(tmp_path) -> None:
    """
    Validate category filter behavior.

    Args:
        tmp_path: Temporary directory fixture.

    Returns:
        None.
    """

    (tmp_path / "commercial_slab.jpg").write_bytes(b"binary")
    (tmp_path / "res_foundation.png").write_bytes(b"binary")

    service = GalleryService(gallery_directory=str(tmp_path))
    filtered = service.list_items(category="Commercial")

    assert len(filtered) == 1
    assert filtered[0].category == "Commercial"
