import httpx

WEBHOOK_URL = "http://127.0.0.1:8000/api/v1/webhooks/edr"
API_KEY = "mock-edr-secret"


class MockEDRIntegration:
    """
    Integration layer for sending alerts from the Mock EDR service.

    Currently this only simulates sending alerts.
    In the future, this layer can be replaced with
    real EDR integrations such as CrowdStrike Falcon
    or Microsoft Defender without affecting the rest
    of the project.
    """

    def send_alert(self, alert):
        """
        Send the alert to the webhook endpoint.
        """

        response = httpx.post(
            WEBHOOK_URL,
            headers={
                "X-API-Key": API_KEY
            },
            json=alert.model_dump(mode="json")
        )

        print(f"Status Code : {response.status_code}")
        print(response.json())

        return response