import pytest
from unittest.mock import MagicMock

from app.services.evidence_collection_service import EvidenceCollectionService


@pytest.fixture
def service():
    return EvidenceCollectionService()


def test_collect_kape_calls_live_response_client(service):
    expected = {
        "status": "success",
        "action": "execute_kape",
        "hostname": "FINANCE-PC",
        "message": "KAPE collection completed successfully."
    }

    service.live_response_client.execute_kape = MagicMock(return_value=expected)

    result = service.collect_kape("FINANCE-PC")

    service.live_response_client.execute_kape.assert_called_once_with("FINANCE-PC")
    assert result == expected


def test_capture_ram_calls_live_response_client(service):
    expected = {
        "status": "success",
        "action": "capture_memory",
        "hostname": "FINANCE-PC",
        "message": "Memory acquisition completed successfully."
    }

    service.live_response_client.capture_memory = MagicMock(return_value=expected)

    result = service.capture_ram("FINANCE-PC")

    service.live_response_client.capture_memory.assert_called_once_with("FINANCE-PC")
    assert result == expected