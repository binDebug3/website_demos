"""
Domain models and operations for lead intake.
"""

import logging

import httpx
from pydantic import BaseModel, Field

from forshor.config import settings

LOGGER = logging.getLogger(__name__)


class LeadCreate(BaseModel):
    """
    Input schema for a new lead submission.

    Attributes:
        name: Contact person full name.
        company: Company name.
        phone: Primary callback number.
        details: Freeform description of requested items or timeline.
    """

    name: str = Field(min_length=2, max_length=120)
    company: str = Field(min_length=2, max_length=120)
    phone: str = Field(min_length=7, max_length=30)
    details: str = Field(min_length=5, max_length=1500)


class LeadSubmissionResult(BaseModel):
    """
    Result of a lead submission operation.

    Attributes:
        accepted: Indicates whether submission reached Formspree.
        message: Human-readable status message.
    """

    accepted: bool
    message: str


class LeadService:
    """
    Encapsulates stateless lead forwarding to Formspree.
    """

    def submit_lead(
        self,
        payload: LeadCreate,
        client: httpx.Client | None = None,
    ) -> LeadSubmissionResult:
        """
        Forward a lead payload to Formspree when configured.

        Args:
            payload: Validated lead submission payload.
            client: Optional HTTP client for testability.

        Returns:
            Submission result for UI and API consumers.
        """

        LOGGER.info("Processing lead submission for %s", payload.company)
        if not settings.formspree_endpoint.strip():
            LOGGER.warning("Formspree endpoint is not configured")
            return LeadSubmissionResult(
                accepted=False,
                message=(
                    "Submission captured locally only. Configure FORSHOR_FORMSPREE_ENDPOINT"
                    " to forward leads."
                ),
            )

        request_client = client or httpx.Client(timeout=15.0)
        should_close = client is None
        try:
            response = request_client.post(
                settings.formspree_endpoint,
                data=payload.model_dump(),
                headers={"Accept": "application/json"},
            )
            response.raise_for_status()
            LOGGER.info("Lead forwarded to Formspree for %s", payload.company)
            return LeadSubmissionResult(
                accepted=True,
                message="Lead sent successfully. We will contact you soon.",
            )
        except httpx.HTTPError as exc:
            LOGGER.exception("Formspree forwarding failed: %s", exc)
            return LeadSubmissionResult(
                accepted=False,
                message="Lead forwarding failed. Please call us directly.",
            )
        finally:
            if should_close:
                request_client.close()
