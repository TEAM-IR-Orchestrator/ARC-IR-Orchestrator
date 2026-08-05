from datetime import datetime

from app.orchestrator.incident_orchestrator import IncidentOrchestrator
from app.services.threat_evaluator import ThreatEvaluator
from app.schemas.parsed_alert import ParsedAlert


def build_alert(rule_level: int):

    return ParsedAlert(
        alert_id="ALERT-001",
        provider="WAZUH",
        severity="Medium",
        rule_level=rule_level,
        rule_id="5503",
        timestamp=datetime.now(),

        hostname="Ubuntu-desktop",
        ip_address="192.168.29.209",
        device_id="001",
        source_ip=None,

        username="ubuntu80",

        process_name=None,
        process_hash=None,

        title="PAM Login Failed",
        description="Authentication failure",

        groups=["authentication_failed"],

        mitre_id=["T1110.001"],
        mitre_technique=["Password Guessing"],
        mitre_tactic=["Credential Access"],

        event_data={},
    )


def test_low_level_alert():

    orchestrator = IncidentOrchestrator()

    alert = build_alert(5)

    decision = ThreatEvaluator().evaluate(alert)

    if decision:
        orchestrator.process(decision)


def test_high_level_alert():

    orchestrator = IncidentOrchestrator()

    alert = build_alert(14)

    decision = ThreatEvaluator().evaluate(alert)

    if decision:
        orchestrator.process(decision)