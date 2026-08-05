from app.core.logger import get_logger
from app.models.threat_decision import ThreatDecision
from app.playbooks.base_playbook import BasePlaybook
from app.services.containment_service import ContainmentService
from app.services.identity_service import IdentityService
from app.schemas.parsed_alert import ParsedAlert

logger = get_logger(__name__)


class RansomwarePlaybook(BasePlaybook):
    """
    Executes the ransomware containment workflow.
    """

    def __init__(self):

        self.containment = ContainmentService()
        self.identity = IdentityService()

    @property
    def name(self) -> str:
        return "RANSOMWARE_CONTAINMENT"

    def execute(
        self,
        decision: ThreatDecision,
        alert: ParsedAlert,
    ):

        logger.info(
            "Starting playbook '%s' for host '%s'.",
            self.name,
            decision.hostname,
        )

        # Network Containment
        containment_result = self.containment.contain_host(
            agent_id=decision.device_id,
            hostname=decision.hostname,
            alert=alert
        )

        logger.info(
            "Containment result: %s",
            containment_result,
        )

        # Suspend User
        suspend_result = self.identity.suspend_user(
            decision.username
        )

        logger.info(
            "User suspension result: %s",
            suspend_result,
        )

        # Revoke Sessions
        revoke_result = self.identity.revoke_user_sessions(
            decision.username
        )

        logger.info(
            "Session revocation result: %s",
            revoke_result,
        )

        logger.info(
            "Playbook '%s' completed successfully.",
            self.name,
        )