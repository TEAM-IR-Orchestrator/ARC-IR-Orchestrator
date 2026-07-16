from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RawAlert(BaseModel):
    provider: str = "MANUAL"

    alert_id: str
    severity: str
    timestamp: datetime

    hostname: str
    ip_address: str
    device_id: Optional[str] = None

    username: str

    process_name: str
    process_hash: str

    title: Optional[str] = None
    description: Optional[str] = None