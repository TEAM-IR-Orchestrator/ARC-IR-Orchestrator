from app.analysis.behavior_engine import BehaviorEngine
from app.analysis.context_engine import ContextEngine
from app.analysis.mitre_engine import MitreEngine
from app.analysis.rule_engine import RuleEngine

from app.models.threat_context import ThreatContext
from app.models.threat_decision import ThreatDecision

from app.policies.policy_engine import PolicyEngine

from app.schemas.parsed_alert import ParsedAlert


class ThreatEvaluator:
    """
    Enterprise Threat Evaluation Pipeline.

    This service orchestrates all analyzers and the policy engine.
    It never contains detection logic itself.
    """

    def __init__(self):

        self.rule_analyzer = RuleEngine()

        self.mitre_analyzer = MitreEngine()

        self.behavior_analyzer = BehaviorEngine()

        self.context_analyzer = ContextEngine()

        self.policy_engine = PolicyEngine()

    def evaluate(
        self,
        alert: ParsedAlert,
        ) -> ThreatDecision | None:

        rule_analysis = self.rule_analyzer.evaluate(alert)

        mitre_analysis = self.mitre_analyzer.evaluate(alert)

        behavior_analysis = self.behavior_analyzer.evaluate(alert)

        context_analysis = self.context_analyzer.evaluate(alert)

        total_score = (
            rule_analysis.score
            + mitre_analysis.score
            + behavior_analysis.score
            + context_analysis.score
        )

        analysis = ThreatContext(

            rule_score=rule_analysis.score,

            mitre_score=mitre_analysis.score,

            behavior_score=behavior_analysis.score,

            context_score=context_analysis.score,

            total_score=total_score,

            reasons=[
                *rule_analysis.reasons,
                *mitre_analysis.reasons,
                *behavior_analysis.reasons,
                *context_analysis.reasons,
            ],

            matched_rule_ids=rule_analysis.matched_rule_ids,

            matched_mitre_ids=mitre_analysis.matched_mitre_ids,
        )

        return self.policy_engine.evaluate(
            alert,
            analysis,
        )