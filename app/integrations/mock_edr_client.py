import random


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
        and return one of several realistic containment
        responses from a mock Enterprise EDR.
        """

        print(f"[MockEDR] Sending network containment command for host: {hostname}")

        # Predefined mock containment responses used to simulate
        # different Enterprise EDR network isolation outcomes.
        responses = [
            {
                "status": "success",
                "action": "network_containment",
                "message": "Host successfully isolated."
            },
            {
                "status": "success",
                "action": "network_containment",
                "message": "Host is already isolated."
            },
            {
                "status": "failed",
                "action": "network_containment",
                "message": "Host not found."
            },
            {
                "status": "failed",
                "action": "network_containment",
                "message": "Unable to communicate with endpoint."
            }
        ]

        response = random.choice(responses)

        return {
            "status": response["status"],
            "action": response["action"],
            "hostname": hostname,
            "message": response["message"]
        }