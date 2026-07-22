from app.schemas.parsed_alert import ParsedAlert

class IncidentOrchestrator:
    """
    Coordinates the complete incident response workflow.

    Current Status:
    - Receives standardized ParsedAlert objects.
    - Future weeks will add automated containment,
      memory capture, account suspension, etc.
    """

    def process_incident(self, parsed_alert: ParsedAlert):
        print("Incident Orchestrator received alert.")
        print(parsed_alert)