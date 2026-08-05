from app.models.threat_context import ThreatContext
from app.models.threat_decision import ThreatDecision
from app.policies.base_policy import BasePolicy
from app.policies.ransomware_policy import RansomwarePolicy
from app.schemas.parsed_alert import ParsedAlert


class PolicyEngine:
    """
    Evaluates all registered security policies.

    The engine is policy-agnostic and simply selects the
    highest-priority matching policy.
    """

    def __init__(self):

        self._policies: list[BasePolicy] = [

            RansomwarePolicy(),

        ]

        self._policies.sort(
            key=lambda policy: policy.priority,
            reverse=True,
        )

    def evaluate(
        self,
        alert: ParsedAlert,
        analysis: ThreatContext,
    ) -> ThreatDecision | None:

        for policy in self._policies:

            if policy.matches(alert, analysis):

                return policy.build_decision(
                    alert,
                    analysis,
                )

        return None