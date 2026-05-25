"""
Lead and quote submission routes.
"""

from fastapi import APIRouter, Depends, Form, status
from fastapi.responses import RedirectResponse

from forshor.api.dependencies import get_lead_service
from forshor.domain.lead_service import LeadCreate, LeadService, LeadSubmissionResult

router = APIRouter(prefix="/api/leads", tags=["leads"])


@router.post(
    "", response_model=LeadSubmissionResult, status_code=status.HTTP_201_CREATED
)
def create_lead(
    payload: LeadCreate,
    lead_service: LeadService = Depends(get_lead_service),
) -> LeadSubmissionResult:
    """
    Create a new quote/contact lead.

    Args:
        payload: Validated lead input payload.
        lead_service: Domain service for lead operations.

    Returns:
        Submission status.
    """

    return lead_service.submit_lead(payload=payload)


@router.post("/form", status_code=status.HTTP_303_SEE_OTHER)
def create_lead_from_form(
    name: str = Form(...),
    company: str = Form(...),
    phone: str = Form(...),
    details: str = Form(...),
    lead_service: LeadService = Depends(get_lead_service),
) -> RedirectResponse:
    """
    Create a lead from standard HTML form data.

    Args:
        name: Contact full name.
        company: Company name.
        phone: Callback number.
        details: Freeform request details.
        lead_service: Domain service for lead operations.

    Returns:
        Redirect to landing page with status indicator.
    """

    payload = LeadCreate(
        name=name,
        company=company,
        phone=phone,
        details=details,
    )
    result = lead_service.submit_lead(payload=payload)
    status_param = "sent" if result.accepted else "error"
    return RedirectResponse(url=f"/?quote_status={status_param}", status_code=303)
