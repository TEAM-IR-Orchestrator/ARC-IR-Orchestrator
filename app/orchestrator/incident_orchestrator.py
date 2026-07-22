from app.schemas.parsed_alert import ParsedAlert
from app.services.containment_service import ContainmentService


class IncidentOrchestrator:
    """
    Coordinates the complete incident response workflow.

    Current Status:
    - Receives standardized ParsedAlert objects.
    - Decides whether automated containment is required.
    - Delegates containment actions to the ContainmentService.

    Future Weeks:
    - Account suspension
    - Session revocation
    - Memory acquisition
    - Evidence collection
    """

    def __init__(self):
        self.containment_service = ContainmentService()

    def process_incident(self, parsed_alert: ParsedAlert):
        print("Incident Orchestrator received alert.")
        print(parsed_alert)

        # Execute containment only for High and Critical alerts
        if parsed_alert.severity.lower() in ["high", "critical"]:

            print(
                f"[IncidentOrchestrator] "
                f"Severity '{parsed_alert.severity}' requires containment."
            )

            result = self.containment_service.contain_host(
                parsed_alert.hostname
            )

            print(result)

        else:
            print(
                f"[IncidentOrchestrator] "
                f"No containment required for '{parsed_alert.severity}' alerts."
            )