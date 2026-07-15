from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ParsedAlert(BaseModel):
    # Alert Information
    alert_id: str
    provider: str
    severity: str
    timestamp: datetime

    # Device Information
    hostname: str
    ip_address: str
    device_id: Optional[str] = None

    # User Information
    username: str

    # Process Information
    process_name: str
    process_hash: str

    # Alert Details
    title: Optional[str] = None
    description: Optional[str] = None