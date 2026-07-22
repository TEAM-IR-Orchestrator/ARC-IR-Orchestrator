from app.integrations.mock_edr_client import MockEDRClient


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

        result = self.edr_client.isolate_host(hostname)

        print("[ContainmentService] Network containment completed.")

        return result