import httpx

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

        webhook_url = "http://127.0.0.1:8000/api/v1/webhooks/edr"

        response = httpx.post(
            webhook_url,
            headers={
                "X-API-Key": "mock-edr-secret"
            },
            json=alert.model_dump(mode="json")
    )

        print(f"Status Code : {response.status_code}")
        print(response.json())

        return response