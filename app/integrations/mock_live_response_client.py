import random


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

        # Predefined mock responses for KAPE collection.
        responses = [
            {
                "status": "success",
                "action": "execute_kape",
                "message": "KAPE collection completed successfully."
            },
            {
                "status": "success",
                "action": "execute_kape",
                "message": "KAPE collection already running."
            },
            {
                "status": "failed",
                "action": "execute_kape",
                "message": "Endpoint not reachable."
            },
            {
                "status": "failed",
                "action": "execute_kape",
                "message": "Failed to start KAPE collection."
            }
        ]

        response = random.choice(responses)

        return {
            "status": response["status"],
            "action": response["action"],
            "hostname": hostname,
            "message": response["message"]
        }

    def capture_memory(self, hostname: str):
        """
        Simulate remotely capturing
        a memory dump from the endpoint.
        """

        # Predefined mock responses for memory acquisition.
        responses = [
            {
                "status": "success",
                "action": "capture_memory",
                "message": "Memory acquisition completed successfully."
            },
            {
                "status": "success",
                "action": "capture_memory",
                "message": "Memory acquisition already in progress."
            },
            {
                "status": "failed",
                "action": "capture_memory",
                "message": "Endpoint not reachable."
            },
            {
                "status": "failed",
                "action": "capture_memory",
                "message": "Failed to capture memory."
            }
        ]

        response = random.choice(responses)

        return {
            "status": response["status"],
            "action": response["action"],
            "hostname": hostname,
            "message": response["message"]
        }
    