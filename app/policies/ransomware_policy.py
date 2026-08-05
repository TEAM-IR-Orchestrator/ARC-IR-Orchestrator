from app.models.threat_context import ThreatContext
from app.models.threat_decision import ThreatDecision
from app.policies.base_policy import BasePolicy
from app.schemas.parsed_alert import ParsedAlert


class RansomwarePolicy(BasePolicy):
    """
    Enterprise ransomware response policy.

    This policy correlates multiple independent signals before
    authorizing automated containment.
    """

    @property
    def name(self) -> str:
        return "RansomwarePolicy"

    @property
    def priority(self) -> int:
        return 100

    def matches(
        self,
        alert: ParsedAlert,
        analysis: ThreatContext,
    ) -> bool:

        mitre_detected = (
            "T1486" in analysis.matched_mitre_ids
        )

        high_rule = (
            alert.rule_level >= 12
        )

        suspicious_behavior = (
            analysis.behavior_score >= 40
        )

        total_risk = (
            analysis.total_score >= 90
        )

        #
        # Enterprise policy:
        #
        # Ransomware technique
        # AND
        # (High severity OR Strong behaviour)
        #
        if (
            mitre_detected
            and
            (high_rule or suspicious_behavior)
        ):
            return True

        #
        # Extremely high overall risk
        #
        if total_risk:
            return True

        return False

    def build_decision(
        self,
        alert: ParsedAlert,
        analysis: ThreatContext,
    ) -> ThreatDecision:

        return ThreatDecision(

            # Decision
            should_trigger_playbook=True,

            playbook_name="RANSOMWARE_CONTAINMENT",

            matched_policy=self.name,

            # Risk
            score=analysis.total_score,

            severity="Critical",

            confidence="High",

            priority=self.priority,

            # Execution Context
            hostname=alert.hostname,

            device_id=alert.device_id,

            username=alert.username,

            source_ip=alert.source_ip,

            # Explainability
            reasons=analysis.reasons,

            matched_rule_ids=analysis.matched_rule_ids,

            matched_mitre_ids=analysis.matched_mitre_ids,
        )