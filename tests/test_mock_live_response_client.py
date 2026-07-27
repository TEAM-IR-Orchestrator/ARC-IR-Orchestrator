import pytest
from unittest.mock import patch

from app.integrations.mock_live_response_client import MockLiveResponseClient


@pytest.fixture
def client():
    return MockLiveResponseClient()


# ---------------------------
# KAPE Collection Tests
# ---------------------------

def test_execute_kape_success(client):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "success",
            "action": "execute_kape",
            "message": "KAPE collection completed successfully."
        }

        result = client.execute_kape("FINANCE-PC")

        assert result["status"] == "success"
        assert result["action"] == "execute_kape"
        assert result["hostname"] == "FINANCE-PC"
        assert result["message"] == "KAPE collection completed successfully."


def test_execute_kape_already_running(client):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "success",
            "action": "execute_kape",
            "message": "KAPE collection already running."
        }

        result = client.execute_kape("FINANCE-PC")

        assert result["status"] == "success"
        assert result["action"] == "execute_kape"
        assert result["hostname"] == "FINANCE-PC"
        assert result["message"] == "KAPE collection already running."


def test_execute_kape_endpoint_not_reachable(client):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "failed",
            "action": "execute_kape",
            "message": "Endpoint not reachable."
        }

        result = client.execute_kape("FINANCE-PC")

        assert result["status"] == "failed"
        assert result["action"] == "execute_kape"
        assert result["hostname"] == "FINANCE-PC"
        assert result["message"] == "Endpoint not reachable."


def test_execute_kape_failure(client):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "failed",
            "action": "execute_kape",
            "message": "Failed to start KAPE collection."
        }

        result = client.execute_kape("FINANCE-PC")

        assert result["status"] == "failed"
        assert result["action"] == "execute_kape"
        assert result["hostname"] == "FINANCE-PC"
        assert result["message"] == "Failed to start KAPE collection."


# ---------------------------
# Memory Collection Tests
# ---------------------------

def test_capture_memory_success(client):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "success",
            "action": "capture_memory",
            "message": "Memory acquisition completed successfully."
        }

        result = client.capture_memory("FINANCE-PC")

        assert result["status"] == "success"
        assert result["action"] == "capture_memory"
        assert result["hostname"] == "FINANCE-PC"
        assert result["message"] == "Memory acquisition completed successfully."


def test_capture_memory_already_running(client):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "success",
            "action": "capture_memory",
            "message": "Memory acquisition already in progress."
        }

        result = client.capture_memory("FINANCE-PC")

        assert result["status"] == "success"
        assert result["action"] == "capture_memory"
        assert result["hostname"] == "FINANCE-PC"
        assert result["message"] == "Memory acquisition already in progress."


def test_capture_memory_endpoint_not_reachable(client):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "failed",
            "action": "capture_memory",
            "message": "Endpoint not reachable."
        }

        result = client.capture_memory("FINANCE-PC")

        assert result["status"] == "failed"
        assert result["action"] == "capture_memory"
        assert result["hostname"] == "FINANCE-PC"
        assert result["message"] == "Endpoint not reachable."


def test_capture_memory_failure(client):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "failed",
            "action": "capture_memory",
            "message": "Failed to capture memory."
        }

        result = client.capture_memory("FINANCE-PC")

        assert result["status"] == "failed"
        assert result["action"] == "capture_memory"
        assert result["hostname"] == "FINANCE-PC"
        assert result["message"] == "Failed to capture memory."