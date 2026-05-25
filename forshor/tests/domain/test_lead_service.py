"""
Domain tests for lead submission service.
"""

import httpx

from forshor.config import settings
from forshor.domain.lead_service import LeadCreate, LeadService


class StubClient:
    """
    Simple stub HTTP client for deterministic lead service testing.
    """

    def __init__(self, status_code: int) -> None:
        """
        Build a stub with desired response status.

        Args:
            status_code: HTTP status code to return.
        """

        self._status_code = status_code

    def post(
        self, url: str, data: dict[str, str], headers: dict[str, str]
    ) -> httpx.Response:
        """
        Return a synthetic response object.

        Args:
            url: Target endpoint URL.
            data: Posted lead payload.
            headers: Request headers.

        Returns:
            HTTPX response object.
        """

        request = httpx.Request("POST", url, data=data, headers=headers)
        return httpx.Response(status_code=self._status_code, request=request)


def test_submit_lead_without_formspree_endpoint() -> None:
    """
    Validate graceful behavior when Formspree is not configured.

    Returns:
        None.
    """

    original_endpoint = settings.formspree_endpoint
    settings.formspree_endpoint = ""
    try:
        service = LeadService()
        result = service.submit_lead(
            payload=LeadCreate(
                name="Alex",
                company="Field Ops",
                phone="555-0000",
                details="Need ties.",
            )
        )
        assert result.accepted is False
    finally:
        settings.formspree_endpoint = original_endpoint


def test_submit_lead_with_formspree_success() -> None:
    """
    Validate successful Formspree forwarding.

    Returns:
        None.
    """

    original_endpoint = settings.formspree_endpoint
    settings.formspree_endpoint = "https://formspree.io/f/mock"
    try:
        service = LeadService()
        result = service.submit_lead(
            payload=LeadCreate(
                name="Alex",
                company="Field Ops",
                phone="555-0000",
                details="Need ties.",
            ),
            client=StubClient(status_code=200),
        )
        assert result.accepted is True
    finally:
        settings.formspree_endpoint = original_endpoint


def test_submit_lead_with_formspree_failure() -> None:
    """
    Validate failed Formspree forwarding branch.

    Returns:
        None.
    """

    original_endpoint = settings.formspree_endpoint
    settings.formspree_endpoint = "https://formspree.io/f/mock"
    try:
        service = LeadService()
        result = service.submit_lead(
            payload=LeadCreate(
                name="Alex",
                company="Field Ops",
                phone="555-0000",
                details="Need ties.",
            ),
            client=StubClient(status_code=500),
        )
        assert result.accepted is False
    finally:
        settings.formspree_endpoint = original_endpoint
