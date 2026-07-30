from typing import Any

from pydantic import BaseModel


class RawAlert(BaseModel):
    """
    Raw alert received from a security provider.

    The payload is intentionally kept provider-specific.
    Parsing and normalization are handled by AlertParser.
    """

    provider: str = "WAZUH"
    payload: dict[str, Any]