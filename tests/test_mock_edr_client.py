import pytest

from app.integrations.mock_edr_client import MockEDRClient


@pytest.fixture
def client():
    return MockEDRClient()


def test_network_containment_success(client):
    hostname = "FINANCE-PC"

    result = client.isolate_host(hostname)

    assert result["status"] == "success"
    assert result["action"] == "network_containment"
    assert result["hostname"] == hostname
    assert result["message"] == f"Host '{hostname}' successfully isolated."