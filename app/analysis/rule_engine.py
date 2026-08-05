from app.schemas.parsed_alert import ParsedAlert
from app.models.engine_result import EngineResult

class RuleEngine:
    """
    Evaluates Wazuh-specific rule information.

    Responsible only for scoring based on:
    - Rule Level
    - Rule ID
    - Rule Groups
    """

    HIGH_RULE_LEVEL = 12
    MEDIUM_RULE_LEVEL = 8

    # Rules that should immediately increase confidence.
    # We'll expand this as we build the lab.
    CRITICAL_RULE_IDS = {
        # Example:
        # "87100",
    }

    # Groups frequently associated with high-risk attacks.
    HIGH_RISK_GROUPS = {
        "ransomware",
        "malware",
        "rootkit",
        "web_attack",
        "privilege_escalation",
        "persistence",
        "lateral_movement",
        "active_response",
    }

    def evaluate(self, alert: ParsedAlert) -> dict:
        """
        Returns the rule evaluation result.
        """

        score = 0
        reasons = []

        # Rule Level
        if alert.rule_level >= self.HIGH_RULE_LEVEL:
            score += 40
            reasons.append(
                f"Wazuh rule level {alert.rule_level} indicates a high severity event."
            )

        elif alert.rule_level >= self.MEDIUM_RULE_LEVEL:
            score += 20
            reasons.append(
                f"Wazuh rule level {alert.rule_level} indicates a medium severity event."
            )

        # Rule ID
        if alert.rule_id in self.CRITICAL_RULE_IDS:
            score += 30
            reasons.append(
                f"Rule ID {alert.rule_id} is marked as critical."
            )

        # Groups
        if alert.groups:
            matched = [
                group
                for group in alert.groups
                if group.lower() in self.HIGH_RISK_GROUPS
            ]

            if matched:
                score += 20
                reasons.append(
                    f"Matched high-risk groups: {', '.join(matched)}"
                )

        return EngineResult(
            score=score,
            reasons=reasons,
            matched_rule_ids=[alert.rule_id],
        )