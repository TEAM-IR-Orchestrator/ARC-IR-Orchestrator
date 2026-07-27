class MockLiveResponseClient:
    """
    Simulates an Enterprise EDR Live Response client.

    This class represents the remote execution capability
    provided by Enterprise EDR platforms such as CrowdStrike
    Falcon Real Time Response or Microsoft Defender Live Response.

    It is responsible only for executing forensic acquisition
    commands on compromised endpoints.
    Business logic should not exist here.
    """

    def execute_kape(self, hostname: str):
        """
        Simulate remotely executing KAPE
        on the compromised endpoint.
        """
        pass

    def capture_memory(self, hostname: str):
        """
        Simulate remotely capturing
        a memory dump from the endpoint.
        """
        pass