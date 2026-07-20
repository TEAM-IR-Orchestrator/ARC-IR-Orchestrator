from datetime import datetime

from app.schemas.raw_alert import RawAlert


class MockEDR:
    def generate_mock_alert(self) -> RawAlert:
        return RawAlert(
            provider="MANUAL",
            alert_id="mock-alert-001",
            severity="critical",
            timestamp=datetime.now(),
            hostname="DESKTOP-01",
            ip_address="192.168.1.10",
            username="john.doe",
            process_name="encryptor.exe",
            process_hash="ABC123XYZ",
            title="Mock Ransomware Alert",
            description="Testing webhook ingestion",
        )
    
    