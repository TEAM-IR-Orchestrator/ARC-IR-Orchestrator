from app.schemas.parsed_alert import ParsedAlert
from app.models.engine_result import EngineResult

class BehaviorEngine:
    """
    Evaluates attacker behavior based on
    Wazuh rule groups, event content and process activity.
    """

    HIGH_RISK_GROUPS = {
        "ransomware": 50,
        "malware": 40,
        "rootkit": 40,
        "persistence": 30,
        "privilege_escalation": 25,
        "defense_evasion": 25,
        "lateral_movement": 30,
        "credential_access": 20,
    }

    HIGH_RISK_KEYWORDS = {
        "vssadmin": 40,
        "wbadmin": 40,
        "bcdedit": 35,
        "cipher.exe": 30,
        "mimikatz": 50,
        "psexec": 30,
        "rclone": 25,
        "encrypt": 50,
        "ransom": 50,
        "shadow copy": 40,
        "delete shadows": 45,
    }

    def evaluate(self, alert: ParsedAlert):

        score = 0
        reasons = []

        # Wazuh Groups
        for group in alert.groups:
            if group.lower() in self.HIGH_RISK_GROUPS:
                value = self.HIGH_RISK_GROUPS[group.lower()]
                score += value
                reasons.append(
                    f"High-risk behavior group detected: {group} (+{value})"
                )

        # Process Name
        if alert.process_name:
            process = alert.process_name.lower()

            for keyword, value in self.HIGH_RISK_KEYWORDS.items():
                if keyword in process:
                    score += value
                    reasons.append(
                        f"Suspicious process detected: {process} (+{value})"
                    )

        # Full Event
        if alert.description:

            text = alert.description.lower()

            for keyword, value in self.HIGH_RISK_KEYWORDS.items():
                if keyword in text:
                    score += value
                    reasons.append(
                        f"Suspicious behaviour detected: '{keyword}' (+{value})"
                    )

        return EngineResult(
            score=score,
            reasons=reasons,
        )