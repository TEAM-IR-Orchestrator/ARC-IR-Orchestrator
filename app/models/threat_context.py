from pydantic import BaseModel, Field


class ThreatContext(BaseModel):
    """
    Combined analysis produced by all analyzers.
    """

    total_score: int = 0

    reasons: list[str] = Field(default_factory=list)

    matched_rule_ids: list[str] = Field(default_factory=list)

    matched_mitre_ids: list[str] = Field(default_factory=list)

    behavior_score: int = 0

    context_score: int = 0

    rule_score: int = 0

    mitre_score: int = 0