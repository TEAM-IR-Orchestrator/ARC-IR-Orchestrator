from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ParsedAlert(BaseModel):

    # Alert Information
    alert_id: str
    provider: str
    severity: str
    rule_level: int
    rule_id: str
    timestamp: datetime

    # Device
    hostname: str
    ip_address: str
    device_id: Optional[str] = None
    source_ip: Optional[str] = None

    # User
    username: Optional[str] = None

    # Process (optional)
    process_name: Optional[str] = None
    process_hash: Optional[str] = None

    # Alert Details
    title: Optional[str] = None
    description: Optional[str] = None

    # Wazuh-specific but still generic
    groups: list[str] = Field(default_factory=list)
    mitre_id: list[str] = Field(default_factory=list)
    mitre_technique: list[str] = Field(default_factory=list)
    mitre_tactic: list[str] = Field(default_factory=list)

    event_data: dict = Field(default_factory=dict)