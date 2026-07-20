from app.integrations.mock_edr_integration import MockEDRIntegration
from app.services.mock_edr import MockEDR


def main():
    mock_edr = MockEDR()
    integration = MockEDRIntegration()

    alert = mock_edr.generate_mock_alert()

    integration.send_alert(alert)


if __name__ == "__main__":
    main()