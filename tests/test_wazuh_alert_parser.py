from datetime import datetime

import pytest

from app.services.alert_parser import AlertParser


@pytest.fixture
def parser():
    return AlertParser()


@pytest.fixture
def wazuh_alert():
    return {
        "id": "1785582114.93499",

        "@timestamp": "2026-08-01T11:01:54.410Z",

        "agent": {
            "id": "001",
            "name": "Ubuntu-desktop",
            "ip": "192.168.29.209"
        },

        "rule": {
            "id": "5503",
            "level": 5,
            "description": "PAM: User login failed.",
            "groups": [
                "pam",
                "authentication_failed"
            ],
            "mitre": {
                "id": [
                    "T1110.001"
                ],
                "technique": [
                    "Password Guessing"
                ],
                "tactic": [
                    "Credential Access"
                ]
            }
        },

        "data": {
            "srcuser": "ubuntu80",
            "uid": "1000",
            "euid": "0"
        },

        "full_log": "authentication failure"
    }


def test_provider(parser, wazuh_alert):

    parsed = parser.parse(
        wazuh_alert,
        "WAZUH",
    )

    assert parsed.provider == "WAZUH"


def test_hostname(parser, wazuh_alert):

    parsed = parser.parse(
        wazuh_alert,
        "WAZUH",
    )

    assert parsed.hostname == "Ubuntu-desktop"


def test_rule_level(parser, wazuh_alert):

    parsed = parser.parse(
        wazuh_alert,
        "WAZUH",
    )

    assert parsed.rule_level == 5


def test_rule_id(parser, wazuh_alert):

    parsed = parser.parse(
        wazuh_alert,
        "WAZUH",
    )

    assert parsed.rule_id == "5503"


def test_username(parser, wazuh_alert):

    parsed = parser.parse(
        wazuh_alert,
        "WAZUH",
    )

    assert parsed.username == "ubuntu80"


def test_groups(parser, wazuh_alert):

    parsed = parser.parse(
        wazuh_alert,
        "WAZUH",
    )

    assert "authentication_failed" in parsed.groups


def test_mitre(parser, wazuh_alert):

    parsed = parser.parse(
        wazuh_alert,
        "WAZUH",
    )

    assert "T1110.001" in parsed.mitre_id