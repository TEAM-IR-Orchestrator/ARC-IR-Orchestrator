import pytest

from app.services.alert_parser import AlertParser
from app.schemas.raw_alert import RawAlert


@pytest.fixture
def parser():
    return AlertParser()


@pytest.fixture
def sample_raw_alert():
    return RawAlert(
        provider="MANUAL",
        alert_id="ALERT-001",
        severity="critical",
        timestamp="2026-07-17T10:30:00Z",
        hostname="DESKTOP-001",
        ip_address="192.168.1.100",
        device_id="DEVICE-001",
        username="john.doe",
        process_name="powershell.exe",
        process_hash="4f7c3b2e1d9a8f76543210abcdef1234567890abcdef1234567890abcdef12",
        title="Manual Test Alert",
        description="Test alert generated for parser unit tests",
    )
@pytest.fixture
def parsed_alert(parser, sample_raw_alert):
    return parser.parse(
        alert_data=sample_raw_alert.model_dump(),
        provider=sample_raw_alert.provider,
    )

def test_manual_alert_is_parsed_successfully(parsed_alert):
    assert parsed_alert is not None
    assert parsed_alert.provider == "MANUAL"

def test_critical_severity_remains_critical(parsed_alert):
    assert parsed_alert.severity == "critical"

def test_hostname_is_parsed_correctly(parsed_alert, sample_raw_alert):
    assert parsed_alert.hostname == sample_raw_alert.hostname

def test_username_is_parsed_correctly(parsed_alert, sample_raw_alert):
    assert parsed_alert.username == sample_raw_alert.username

def test_process_hash_is_parsed_correctly(parsed_alert, sample_raw_alert):
    assert parsed_alert.process_hash == sample_raw_alert.process_hash