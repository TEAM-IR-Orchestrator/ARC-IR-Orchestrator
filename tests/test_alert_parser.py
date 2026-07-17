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


def test_manual_alert_is_parsed_successfully(parser, sample_raw_alert):
    parsed = parser.parse(
        alert_data=sample_raw_alert.model_dump(),
        provider=sample_raw_alert.provider,
    )

    assert parsed is not None
    assert parsed.provider == "MANUAL"


def test_critical_severity_remains_critical(parser, sample_raw_alert):
    parsed = parser.parse(
        alert_data=sample_raw_alert.model_dump(),
        provider=sample_raw_alert.provider,
    )

    assert parsed.severity == "critical"


def test_hostname_is_parsed_correctly(parser, sample_raw_alert):
    parsed = parser.parse(
        alert_data=sample_raw_alert.model_dump(),
        provider=sample_raw_alert.provider,
    )

    assert parsed.hostname == sample_raw_alert.hostname


def test_username_is_parsed_correctly(parser, sample_raw_alert):
    parsed = parser.parse(
        alert_data=sample_raw_alert.model_dump(),
        provider=sample_raw_alert.provider,
    )

    assert parsed.username == sample_raw_alert.username


def test_process_hash_is_parsed_correctly(parser, sample_raw_alert):
    parsed = parser.parse(
        alert_data=sample_raw_alert.model_dump(),
        provider=sample_raw_alert.provider,
    )

    assert parsed.process_hash == sample_raw_alert.process_hash