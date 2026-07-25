from unittest.mock import MagicMock

from app.orchestrator.incident_orchestrator import IncidentOrchestrator
from app.schemas.parsed_alert import ParsedAlert


def create_alert(severity: str) -> ParsedAlert:
    return ParsedAlert(
        alert_id="ALERT-001",
        provider="MANUAL",
        severity=severity,
        timestamp="2026-06-13T10:00:00Z",
        hostname="WIN-CLIENT-01",
        ip_address="192.168.1.10",
        device_id="DEVICE-001",
        username="john.doe",
        process_name="malware.exe",
        process_hash="abcdef1234567890",
        title="Malware Detected",
        description="Test alert"
    )


def test_high_severity_executes_full_containment_workflow():
    orchestrator = IncidentOrchestrator()

    orchestrator.containment_service.contain_host = MagicMock(
        return_value={"status": "success"}
    )

    orchestrator.identity_service.suspend_user = MagicMock(
        return_value={"status": "success"}
    )

    orchestrator.identity_service.revoke_user_sessions = MagicMock(
        return_value={"status": "success"}
    )

    alert = create_alert("High")

    orchestrator.process_incident(alert)

    orchestrator.containment_service.contain_host.assert_called_once_with(
        "WIN-CLIENT-01"
    )

    orchestrator.identity_service.suspend_user.assert_called_once_with(
        "john.doe"
    )

    orchestrator.identity_service.revoke_user_sessions.assert_called_once_with(
        "john.doe"
    )


def test_critical_severity_executes_full_containment_workflow():
    orchestrator = IncidentOrchestrator()

    orchestrator.containment_service.contain_host = MagicMock(
        return_value={"status": "success"}
    )

    orchestrator.identity_service.suspend_user = MagicMock(
        return_value={"status": "success"}
    )

    orchestrator.identity_service.revoke_user_sessions = MagicMock(
        return_value={"status": "success"}
    )

    alert = create_alert("Critical")

    orchestrator.process_incident(alert)

    orchestrator.containment_service.contain_host.assert_called_once()
    orchestrator.identity_service.suspend_user.assert_called_once()
    orchestrator.identity_service.revoke_user_sessions.assert_called_once()


def test_low_severity_does_not_execute_containment():
    orchestrator = IncidentOrchestrator()

    orchestrator.containment_service.contain_host = MagicMock()

    orchestrator.identity_service.suspend_user = MagicMock()

    orchestrator.identity_service.revoke_user_sessions = MagicMock()

    alert = create_alert("Low")

    orchestrator.process_incident(alert)

    orchestrator.containment_service.contain_host.assert_not_called()
    orchestrator.identity_service.suspend_user.assert_not_called()
    orchestrator.identity_service.revoke_user_sessions.assert_not_called()