from app.models.threat_decision import ThreatDecision
from app.playbooks.ransomware_playbook import RansomwarePlaybook
from app.schemas.parsed_alert import ParsedAlert
from app.core.logger import get_logger

logger = get_logger(__name__)

class IncidentOrchestrator:
    """
    Central orchestration layer.

    Receives a ThreatDecision from the Threat Evaluator
    and delegates execution to the appropriate playbook.

    The orchestrator never contains response logic.
    """

    def __init__(self):

        self._playbooks = {

            "RANSOMWARE_CONTAINMENT": RansomwarePlaybook(),

        }

    def process(
        self,
        decision: ThreatDecision,
        alert: ParsedAlert,
    ):

        if not decision.should_trigger_playbook:

            logger.info(
                "No playbook triggered."
            )

            return

        playbook = self._playbooks.get(
            decision.playbook_name
        )

        if playbook is None:

            raise ValueError(
                f"Unknown playbook: {decision.playbook_name}"
            )

        logger.info(
            "Executing playbook: %s",
            decision.playbook_name,
        )

        playbook.execute(
            decision=decision,
            alert = alert,
        )

        logger.info(
            "Playbook execution completed."
        )