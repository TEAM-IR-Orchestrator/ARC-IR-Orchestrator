from fastapi import APIRouter

from app.schemas.raw_alert import RawAlert
from app.services.alert_parser import AlertParser
from app.orchestrator.incident_orchestrator import IncidentOrchestrator

router = APIRouter(
    prefix="/api/v1/webhooks",
    tags=["EDR Webhooks"]
)
@router.post("/edr")
async def receive_edr_alert(alert: RawAlert):
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

    