import pytest
from unittest.mock import patch

from app.integrations.mock_edr_client import MockEDRClient


@pytest.fixture
def client():
    return MockEDRClient()

@patch("random.choice")
def test_network_containment_success(mock_choice, client):
    hostname = "FINANCE-PC"

    mock_choice.return_value = {
        "status": "success",
        "action": "network_containment",
        "message": "Host successfully isolated."
    }

    result = client.isolate_host(hostname)

    assert result["status"] == "success"
    assert result["action"] == "network_containment"
    assert result["hostname"] == hostname
    assert result["message"] == "Host successfully isolated."    

@patch("random.choice")
def test_host_already_isolated(mock_choice, client):
    hostname = "FINANCE-PC"

    mock_choice.return_value = {
        "status": "success",
        "action": "network_containment",
        "message": "Host is already isolated."
    }

    result = client.isolate_host(hostname)

    assert result["status"] == "success"
    assert result["message"] == "Host is already isolated."

@patch("random.choice")
def test_host_not_found(mock_choice, client):
    hostname = "FINANCE-PC"

    mock_choice.return_value = {
        "status": "failed",
        "action": "network_containment",
        "message": "Host not found."
    }

    result = client.isolate_host(hostname)

    assert result["status"] == "failed"
    assert result["message"] == "Host not found."    

@patch("random.choice")
def test_network_containment_failed(mock_choice, client):
    hostname = "FINANCE-PC"

    mock_choice.return_value = {
        "status": "failed",
        "action": "network_containment",
        "message": "Unable to communicate with endpoint."
    }

    result = client.isolate_host(hostname)

    assert result["status"] == "failed"
    assert result["message"] == "Unable to communicate with endpoint."    