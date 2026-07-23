import pytest
from unittest.mock import patch

from app.services.containment_service import ContainmentService


@pytest.fixture
def service():
    return ContainmentService()

@patch("app.services.containment_service.MockEDRClient.isolate_host")
def test_containment_service_success(mock_isolate, service):
    hostname = "FINANCE-PC"

    mock_isolate.return_value = {
        "status": "success",
        "action": "network_containment",
        "hostname": hostname,
        "message": "Host successfully isolated."
    }

    result = service.contain_host(hostname)

    assert result["status"] == "success"
    assert result["hostname"] == hostname    

@patch("app.services.containment_service.MockEDRClient.isolate_host")
def test_containment_service_already_isolated(mock_isolate, service):
    hostname = "FINANCE-PC"

    mock_isolate.return_value = {
        "status": "success",
        "action": "network_containment",
        "hostname": hostname,
        "message": "Host is already isolated."
    }

    result = service.contain_host(hostname)

    assert result["status"] == "success"
    assert result["message"] == "Host is already isolated."

@patch("app.services.containment_service.MockEDRClient.isolate_host")
def test_containment_service_host_not_found(mock_isolate, service):
    hostname = "FINANCE-PC"

    mock_isolate.return_value = {
        "status": "failed",
        "action": "network_containment",
        "hostname": hostname,
        "message": "Host not found."
    }

    result = service.contain_host(hostname)

    assert result["status"] == "failed"
    assert result["message"] == "Host not found."

@patch("app.services.containment_service.MockEDRClient.isolate_host")
def test_containment_service_failure(mock_isolate, service):
    hostname = "FINANCE-PC"

    mock_isolate.return_value = {
        "status": "failed",
        "action": "network_containment",
        "hostname": hostname,
        "message": "Unable to communicate with endpoint."
    }

    result = service.contain_host(hostname)

    assert result["status"] == "failed"
    assert result["message"] == "Unable to communicate with endpoint."            