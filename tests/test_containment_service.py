import pytest

from app.services.containment_service import ContainmentService


@pytest.fixture
def service():
    return ContainmentService()


def test_containment_service_success(service):
    hostname = "FINANCE-PC"

    result = service.contain_host(hostname)

    assert result["status"] == "success"
    assert result["action"] == "network_containment"
    assert result["hostname"] == hostname
    assert result["message"] == f"Host '{hostname}' successfully isolated."