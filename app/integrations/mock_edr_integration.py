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
        Simulate sending an alert to a webhook.

        Args:
            alert: RawAlert object
        """
        print("Sending alert to webhook...")
        print(alert)