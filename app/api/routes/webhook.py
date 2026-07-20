from fastapi import APIRouter,Header, HTTPException

from app.schemas.raw_alert import RawAlert
from app.services.alert_parser import AlertParser
from app.orchestrator.incident_orchestrator import IncidentOrchestrator


router = APIRouter(
    prefix="/api/v1/webhooks",
    tags=["EDR Webhooks"]
)

def verify_mock_edr_request(api_key: str | None):
    """
    Verify that the incoming webhook request
    is coming from the trusted Mock EDR.
    """

    EXPECTED_API_KEY = "mock-edr-secret"

    if api_key != EXPECTED_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized webhook request",
        )

@router.post("/edr")
async def receive_edr_alert(
    alert: RawAlert,
    x_api_key: str | None = Header(default=None),
):
    verify_mock_edr_request(x_api_key)
    parser = AlertParser()

    parsed_alert = parser.parse(
        alert_data=alert.model_dump(),
        provider=alert.provider,
    )

    orchestrator = IncidentOrchestrator()
    orchestrator.process_incident(parsed_alert)

    return {
        "status": "success",
        "message": "Alert parsed successfully",
        "parsed_alert": parsed_alert.model_dump(),
    }

    