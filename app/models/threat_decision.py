from typing import List, Optional
from pydantic import BaseModel, Field

class ThreatDecision(BaseModel):
    """
    Final decision produced by the Policy Engine.

    This object is the ONLY contract passed from the
    Threat Evaluator to the Incident Orchestrator.
    """

    # Decision
    should_trigger_playbook: bool

    playbook_name: Optional[str] = None

    matched_policy: Optional[str] = None

    # Risk Assessment
    score: int

    severity: str

    confidence: str

    priority: int

    
    # Execution Context
    hostname: str

    device_id: Optional[str] = None

    username: Optional[str] = None

    source_ip: Optional[str] = None

    
    # Explainability
    reasons: List[str] = Field(default_factory=list)

    matched_rule_ids: List[str] = Field(default_factory=list)

    matched_mitre_ids: List[str] = Field(default_factory=list)

    
    # Metadata
    evaluator_version: str = "2.0"