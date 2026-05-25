"""
Server-rendered page routes.
"""

import logging

from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from forshor.api.dependencies import get_gallery_service
from forshor.config import settings
from forshor.domain.gallery_service import GalleryService
from forshor.domain.site_content import (
    FAQ_ENTRIES,
    LOCATION_ENTRIES,
    PARTNERS,
    PRODUCT_ENTRIES,
    get_location_by_slug,
    get_product_by_slug,
)

LOGGER = logging.getLogger(__name__)
router = APIRouter(tags=["pages"])
templates = Jinja2Templates(directory="src/forshor/templates")


def _base_context(request: Request) -> dict[str, object]:
    """
    Build context shared by all page templates.

    Args:
        request: Incoming request.

    Returns:
        Base template context dictionary.
    """

    LOGGER.info("Building base page context for %s", request.url.path)
    return {
        "request": request,
        "app_name": settings.app_name,
        "locations": LOCATION_ENTRIES,
    }


@router.get("/", response_class=HTMLResponse)
def home_page(
    request: Request,
    quote_status: str | None = Query(default=None),
    gallery_service: GalleryService = Depends(get_gallery_service),
) -> HTMLResponse:
    """
    Render the landing page.

    Args:
        request: Incoming request.
        quote_status: Optional quote result indicator.
        gallery_service: Gallery metadata service.

    Returns:
        Rendered HTML page.
    """

    LOGGER.info("Rendering home page")
    context = _base_context(request=request)
    context.update(
        {
            "gallery_items": gallery_service.list_items(),
            "quote_status": quote_status,
            "partners": PARTNERS,
            "page_title": "Industrial-Grade Forming and Shoring",
        }
    )
    return templates.TemplateResponse(
        request=request, name="home.html", context=context
    )


@router.get("/about", response_class=HTMLResponse)
def about_page(request: Request) -> HTMLResponse:
    """
    Render the company overview page.

    Args:
        request: Incoming request.

    Returns:
        Rendered HTML page.
    """

    LOGGER.info("Rendering about page")
    context = _base_context(request=request)
    context.update({"page_title": "Our Company", "active_about": "company"})
    return templates.TemplateResponse(
        request=request, name="about.html", context=context
    )


@router.get("/careers", response_class=HTMLResponse)
def careers_page(request: Request) -> HTMLResponse:
    """
    Render careers page.

    Args:
        request: Incoming request.

    Returns:
        Rendered HTML page.
    """

    LOGGER.info("Rendering careers page")
    context = _base_context(request=request)
    context.update({"page_title": "Job Openings", "active_about": "careers"})
    return templates.TemplateResponse(
        request=request, name="careers.html", context=context
    )


@router.get("/contact", response_class=HTMLResponse)
def contact_page(request: Request) -> HTMLResponse:
    """
    Render contact page.

    Args:
        request: Incoming request.

    Returns:
        Rendered HTML page.
    """

    LOGGER.info("Rendering contact page")
    context = _base_context(request=request)
    context.update({"page_title": "Contact", "active_about": "contact"})
    return templates.TemplateResponse(
        request=request, name="contact.html", context=context
    )


@router.get("/faqs", response_class=HTMLResponse)
def faqs_page(request: Request) -> HTMLResponse:
    """
    Render FAQ page.

    Args:
        request: Incoming request.

    Returns:
        Rendered HTML page.
    """

    LOGGER.info("Rendering faqs page")
    context = _base_context(request=request)
    context.update(
        {
            "page_title": "Frequently Asked Questions",
            "faqs": FAQ_ENTRIES,
            "active_about": "faqs",
        }
    )
    return templates.TemplateResponse(
        request=request, name="faqs.html", context=context
    )


@router.get("/locations", response_class=HTMLResponse)
def locations_page(request: Request) -> HTMLResponse:
    """
    Render list of service locations.

    Args:
        request: Incoming request.

    Returns:
        Rendered HTML page.
    """

    LOGGER.info("Rendering locations page")
    context = _base_context(request=request)
    context.update({"page_title": "Our Utah Locations", "active_about": "locations"})
    return templates.TemplateResponse(
        request=request, name="locations.html", context=context
    )


@router.get("/locations/{location_slug}", response_class=HTMLResponse)
def location_detail_page(request: Request, location_slug: str) -> HTMLResponse:
    """
    Render location detail page.

    Args:
        request: Incoming request.
        location_slug: Route slug for location.

    Returns:
        Rendered HTML page.
    """

    LOGGER.info("Rendering location detail page for %s", location_slug)
    location = get_location_by_slug(slug=location_slug)
    context = _base_context(request=request)
    context.update(
        {
            "location": location,
            "page_title": "Location",
            "active_about": "locations",
        }
    )
    return templates.TemplateResponse(
        request=request, name="location_detail.html", context=context
    )


@router.get("/products", response_class=HTMLResponse)
def products_page(
    request: Request,
    item: str | None = Query(default=None),
) -> HTMLResponse:
    """
    Render products and equipment page.

    Args:
        request: Incoming request.
        item: Optional selected product slug.

    Returns:
        Rendered HTML page.
    """

    LOGGER.info("Rendering products page")
    selected_product = get_product_by_slug(slug=item) if item else PRODUCT_ENTRIES[0]
    if selected_product is None:
        selected_product = PRODUCT_ENTRIES[0]
    context = _base_context(request=request)
    context.update(
        {
            "page_title": "Products and Equipment",
            "products": PRODUCT_ENTRIES,
            "selected_product": selected_product,
        }
    )
    return templates.TemplateResponse(
        request=request, name="products.html", context=context
    )
