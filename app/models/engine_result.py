from typing import List

from pydantic import BaseModel, Field


class EngineResult(BaseModel):
    """
    Standard output returned by every risk engine.
    """

    score: int = 0

    reasons: List[str] = Field(default_factory=list)

    matched_rule_ids: List[str] = Field(default_factory=list)

    matched_mitre_ids: List[str] = Field(default_factory=list)