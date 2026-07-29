from app.clients.edr.edr_client import MockEDRClient


class ContainmentService:
    """
    Service responsible for executing containment actions
    against compromised endpoints.

    Business logic related to containment should live here,
    while communication with the EDR is delegated to the
    MockEDRClient.
    """

    def __init__(self):
        self.edr_client = MockEDRClient()

    def contain_host(self, hostname: str):
        """
        Execute network containment for the specified host.
        """

        print(f"[ContainmentService] Initiating containment for host: {hostname}")

        # Delegate external communication to the Mock EDR Client
        result = self.edr_client.isolate_host(hostname)

        status = str(result.get("status", "")).lower()
        message = str(result.get("message", "")).lower()

        if status == "success":
            if "already" in message and "isolated" in message:
                print("[ContainmentService] Host is already isolated.")
            else:
                print("[ContainmentService] Network containment completed successfully.")

        elif status == "failed":
            if "not found" in message:
                print("[ContainmentService] Host not found.")
            else:
                print("[ContainmentService] Network containment failed.")

        else:
            print("[ContainmentService] Unknown containment response received.")

        # Return the original response without modification
        return result
    