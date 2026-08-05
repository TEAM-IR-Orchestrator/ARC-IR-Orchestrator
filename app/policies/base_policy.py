from abc import ABC, abstractmethod

from app.models.threat_decision import ThreatDecision
from app.models.threat_context import ThreatContext
from app.schemas.parsed_alert import ParsedAlert


class BasePolicy(ABC):
    """
    Base class for all security policies.

    Every policy determines:
    - Whether it matches an alert.
    - Its execution priority.
    - The resulting ThreatDecision.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique policy name."""
        pass

    @property
    @abstractmethod
    def priority(self) -> int:
        """
        Higher priority policies are evaluated first.
        """
        pass

    @abstractmethod
    def matches(self, alert: ParsedAlert, analysis: dict) -> bool:
        """
        Returns True if this policy should handle the alert.
        """
        pass

    @abstractmethod
    def build_decision(
        self,
        alert: ParsedAlert,
        analysis: ThreatContext,
    ) -> ThreatDecision:
        """
        Creates the final ThreatDecision.
        """
        pass