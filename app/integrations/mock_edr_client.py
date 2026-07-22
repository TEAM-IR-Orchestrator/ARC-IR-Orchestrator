class MockEDRClient:
    """
    Client responsible for communicating with the Mock EDR.

    This class simulates containment actions that would normally
    be performed through a real EDR platform such as CrowdStrike
    Falcon or Microsoft Defender for Endpoint.
    """

    def isolate_host(self, hostname: str):
        """
        Simulate sending a network containment command
        to isolate a compromised host.
        """

        print(f"[MockEDR] Sending network containment command for host: {hostname}")

        return {
            "status": "success",
            "action": "network_containment",
            "hostname": hostname,
            "message": f"Host '{hostname}' successfully isolated."
        }