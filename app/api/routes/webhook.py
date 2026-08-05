from fastapi import APIRouter,Header, HTTPException
from typing import Any

from app.services.alert_parser import AlertParser
from app.orchestrator.incident_orchestrator import IncidentOrchestrator
from app.services.threat_evaluator import ThreatEvaluator
from app.core.config import settings

router = APIRouter(
    prefix="/api/v1/webhooks",
    tags=["EDR Webhooks"]
)

def verify_webhook_request(api_key: str | None):
    """
    Verify that the incoming webhook request
    is coming from the trusted Mock EDR.
    """

    if api_key != settings.WEBHOOK_API_KEY:

        raise HTTPException(
            status_code=401,
            detail="Unauthorized webhook request",
        )

@router.post("/wazuh")
async def receive_wazuh_alert(
    alert: dict[str, Any],
    x_api_key: str | None = Header(default=None),
):
    verify_webhook_request(x_api_key)
    parser = AlertParser()

    parsed_alert = parser.parse(
        alert_data=alert,
        provider="WAZUH",
    )

    evaluator = ThreatEvaluator()
    decision = evaluator.evaluate(parsed_alert)
    orchestrator = IncidentOrchestrator()

    if decision:
        orchestrator.process(
            decision = decision,
            alert = parsed_alert,
        )

    return {
        "status": "success",
        "parsed_alert": parsed_alert.model_dump(),
        "decision": (
            decision.model_dump()
            if decision
            else None
        ),
    }

    