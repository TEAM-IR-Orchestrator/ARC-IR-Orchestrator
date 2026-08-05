from app.schemas.parsed_alert import ParsedAlert
from app.models.engine_result import EngineResult

class MitreEngine:
    """
    Evaluates MITRE ATT&CK techniques and tactics
    associated with the alert.
    """

    # High confidence ransomware / hands-on-keyboard techniques
    HIGH_RISK_TECHNIQUES = {
        "T1486": 50,  # Data Encrypted for Impact (Ransomware)
        "T1489": 40,  # Service Stop
        "T1490": 40,  # Inhibit System Recovery
        "T1562": 35,  # Impair Defenses
        "T1059": 25,  # Command and Scripting Interpreter
        "T1105": 25,  # Ingress Tool Transfer
        "T1021": 20,  # Remote Services
        "T1078": 20,  # Valid Accounts
        "T1110": 10,  # Brute Force
    }

    HIGH_RISK_TACTICS = {
        "Impact": 40,
        "Credential Access": 20,
        "Privilege Escalation": 20,
        "Persistence": 20,
        "Lateral Movement": 25,
        "Defense Evasion": 25,
        "Execution": 15,
    }

    def evaluate(self, alert: ParsedAlert) -> dict:
        score = 0
        reasons = []

        matched_mitre = []

        # Techniques
        if alert.mitre_id:
            for technique in alert.mitre_id:
                if technique in self.HIGH_RISK_TECHNIQUES:
                    points = self.HIGH_RISK_TECHNIQUES[technique]
                    score += points
                    matched_mitre.append(technique)

                    reasons.append(
                        f"MITRE technique {technique} matched (+{points})"
                    )

        # Tactics
        if alert.mitre_tactic:
            for tactic in alert.mitre_tactic:
                if tactic in self.HIGH_RISK_TACTICS:
                    points = self.HIGH_RISK_TACTICS[tactic]
                    score += points

                    reasons.append(
                        f"MITRE tactic '{tactic}' matched (+{points})"
                    )

        return EngineResult(
            score=score,
            reasons=reasons,
            matched_mitre_ids=matched_mitre,
        )