from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ParsedAlert(BaseModel):

    # Alert Information
    alert_id: str
    provider: str
    severity: str
    timestamp: datetime

    # Device
    hostname: str
    ip_address: str
    device_id: Optional[str] = None

    # User
    username: Optional[str] = None

    # Process (optional)
    process_name: Optional[str] = None
    process_hash: Optional[str] = None

    # Alert Details
    title: Optional[str] = None
    description: Optional[str] = None

    # Wazuh-specific but still generic
    rule_id: Optional[str] = None
    groups: list[str] = []
    mitre_id: list[str] = []
    mitre_technique: list[str] = []
    mitre_tactic: list[str] = []

    # Preserve original event-specific fields
    event_data: dict = {}