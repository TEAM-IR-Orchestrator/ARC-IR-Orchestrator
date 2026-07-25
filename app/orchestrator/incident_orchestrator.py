from app.schemas.parsed_alert import ParsedAlert
from app.services.containment_service import ContainmentService
from app.services.identity_service import IdentityService


class IncidentOrchestrator:
    """
    Coordinates the complete incident response workflow.
    """

    def __init__(self):
        self.containment_service = ContainmentService()
        self.identity_service = IdentityService()

    def process_incident(self, parsed_alert: ParsedAlert):
        print("Incident Orchestrator received alert.")
        print(parsed_alert)

        if parsed_alert.severity.lower() in ["high", "critical"]:

            print(
                f"[IncidentOrchestrator] "
                f"Severity '{parsed_alert.severity}' requires containment."
            )

            containment_result = self.containment_service.contain_host(
                parsed_alert.hostname
            )

            print(containment_result)

            suspend_result = self.identity_service.suspend_user(
                parsed_alert.username
            )

            print(suspend_result)

            revoke_result = self.identity_service.revoke_user_sessions(
                parsed_alert.username
            )

            print(revoke_result)

        else:
            print(
                f"[IncidentOrchestrator] "
                f"No containment required for '{parsed_alert.severity}' alerts."
            )