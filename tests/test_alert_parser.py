import pytest

from app.services.alert_parser import AlertParser
from app.schemas.raw_alert import RawAlert


@pytest.fixture
def sample_raw_alert():
    return RawAlert(
        alert_type="manual",
        severity="critical",
        hostname="DESKTOP-001",
        username="john.doe",
        process_hash="4f7c3b2e1d9a8f76543210abcdef1234567890abcdef1234567890abcdef12",
    )


def test_manual_alert_is_parsed_successfully(sample_raw_alert):
    parser = AlertParser()

    parsed = parser.parse(sample_raw_alert)

    assert parsed is not None
    assert parsed.alert_type == "manual"


def test_critical_severity_remains_critical(sample_raw_alert):
    parser = AlertParser()

    parsed = parser.parse(sample_raw_alert)

    assert parsed.severity == "critical"


def test_hostname_is_parsed_correctly(sample_raw_alert):
    parser = AlertParser()

    parsed = parser.parse(sample_raw_alert)

    assert parsed.hostname == "DESKTOP-001"


def test_username_is_parsed_correctly(sample_raw_alert):
    parser = AlertParser()

    parsed = parser.parse(sample_raw_alert)

    assert parsed.username == "john.doe"


def test_process_hash_is_parsed_correctly(sample_raw_alert):
    parser = AlertParser()

    parsed = parser.parse(sample_raw_alert)

    assert (
        parsed.process_hash
        == "4f7c3b2e1d9a8f76543210abcdef1234567890abcdef1234567890abcdef12"
    )