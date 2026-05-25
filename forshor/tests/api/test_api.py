"""
API tests for For Shor endpoints.
"""

from fastapi.testclient import TestClient

from forshor.api.main import app
from forshor.config import settings


def test_healthcheck_returns_ok() -> None:
    """
    Validate service health endpoint.

    Returns:
        None.
    """

    client = TestClient(app)
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home_page_renders_company_name() -> None:
    """
    Validate landing page rendering.

    Returns:
        None.
    """

    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == 200
    assert "FOR SHOR" in response.text
    assert "Our Esteemed Partners" in response.text


def test_about_page_renders() -> None:
    """
    Validate company page route.

    Returns:
        None.
    """

    client = TestClient(app)
    response = client.get("/about")

    assert response.status_code == 200
    assert "Our Company" in response.text


def test_careers_page_renders() -> None:
    """
    Validate careers page route.

    Returns:
        None.
    """

    client = TestClient(app)
    response = client.get("/careers")

    assert response.status_code == 200
    assert "Job Openings" in response.text


def test_faq_page_renders() -> None:
    """
    Validate faqs page route.

    Returns:
        None.
    """

    client = TestClient(app)
    response = client.get("/faqs")

    assert response.status_code == 200
    assert "Frequently Asked Questions" in response.text


def test_locations_page_renders() -> None:
    """
    Validate locations page route.

    Returns:
        None.
    """

    client = TestClient(app)
    response = client.get("/locations")

    assert response.status_code == 200
    assert "Salt Lake City" in response.text


def test_location_detail_page_renders() -> None:
    """
    Validate location detail route.

    Returns:
        None.
    """

    client = TestClient(app)
    response = client.get("/locations/provo-ut")

    assert response.status_code == 200
    assert "Provo" in response.text


def test_products_page_renders() -> None:
    """
    Validate products page route.

    Returns:
        None.
    """

    client = TestClient(app)
    response = client.get("/products")

    assert response.status_code == 200
    assert "Popular Products" in response.text


def test_create_lead_via_json_without_formspree() -> None:
    """
    Validate JSON lead submission behavior without Formspree configuration.

    Returns:
        None.
    """

    client = TestClient(app)
    payload = {
        "name": "Casey Foreman",
        "company": "Northline GC",
        "phone": "(801) 487-1656",
        "details": "Need form ties and release agent for Tuesday pour.",
    }

    response = client.post("/api/leads", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["accepted"] is False
    assert "FORSHOR_FORMSPREE_ENDPOINT" in body["message"]


def test_create_lead_via_form_redirects() -> None:
    """
    Validate HTML form lead submission redirect behavior.

    Returns:
        None.
    """

    client = TestClient(app)
    payload = {
        "name": "Jordan Builder",
        "company": "Solid Span",
        "phone": "(801) 487-1656",
        "details": "Need shore posts and slab accessories this week.",
    }

    response = client.post("/api/leads/form", data=payload, follow_redirects=False)

    assert response.status_code == 303
    assert response.headers["location"] == "/?quote_status=error"


def test_gallery_endpoint_returns_list() -> None:
    """
    Validate gallery endpoint behavior.

    Returns:
        None.
    """

    client = TestClient(app)
    response = client.get("/api/gallery")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_formspree_setting_default_is_empty() -> None:
    """
    Validate default Formspree configuration is empty.

    Returns:
        None.
    """

    assert settings.formspree_endpoint == ""
