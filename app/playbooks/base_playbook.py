from abc import ABC, abstractmethod

from app.models.threat_decision import ThreatDecision


class BasePlaybook(ABC):
    """
    Base class for every incident response playbook.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def execute(
        self,
        decision: ThreatDecision,
    ):
        """
        Execute the response workflow.
        """
        pass