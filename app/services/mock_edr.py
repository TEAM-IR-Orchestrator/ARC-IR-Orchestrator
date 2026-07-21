from datetime import datetime
import random

from app.schemas.raw_alert import RawAlert


class MockEDR:
    def generate_mock_alert(self) -> RawAlert:
        mock_alerts = [
            {
                "severity": "critical",
                "hostname": "DESKTOP-01",
                "ip_address": "192.168.1.10",
                "username": "john.doe",
                "process_name": "encryptor.exe",
                "process_hash": "ABC123XYZ",
                "title": "Mock Ransomware Alert",
                "description": "Testing webhook ingestion",
            },
            {
                "severity": "high",
                "hostname": "FINANCE-PC",
                "ip_address": "192.168.1.21",
                "username": "alice.smith",
                "process_name": "locker.exe",
                "process_hash": "DEF456LMN",
                "title": "Suspicious File Encryption",
                "description": "Potential ransomware activity detected.",
            },
            {
                "severity": "critical",
                "hostname": "HR-LAPTOP",
                "ip_address": "10.0.0.15",
                "username": "bob.jones",
                "process_name": "cryptor.exe",
                "process_hash": "XYZ789ABC",
                "title": "Mass File Encryption",
                "description": "Rapid file encryption behavior detected.",
            },
            {
                "severity": "high",
                "hostname": "FILESERVER-01",
                "ip_address": "172.16.1.50",
                "username": "backup.admin",
                "process_name": "darklock.exe",
                "process_hash": "JKL654QWE",
                "title": "Server Encryption Attempt",
                "description": "Suspicious encryption activity on file server.",
            },
            {
                "severity": "critical",
                "hostname": "SQL-SERVER",
                "ip_address": "10.10.10.5",
                "username": "db.admin",
                "process_name": "payload.exe",
                "process_hash": "MNO852RST",
                "title": "Database Ransomware Detected",
                "description": "Database server targeted by ransomware simulation.",
            },
        ]

        alert = random.choice(mock_alerts)

        return RawAlert(
            provider="MANUAL",
            alert_id=f"mock-alert-{random.randint(1000, 9999)}",
            severity=alert["severity"],
            timestamp=datetime.now(),
            hostname=alert["hostname"],
            ip_address=alert["ip_address"],
            username=alert["username"],
            process_name=alert["process_name"],
            process_hash=alert["process_hash"],
            title=alert["title"],
            description=alert["description"],
        )