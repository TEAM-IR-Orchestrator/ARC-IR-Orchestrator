import pytest
from unittest.mock import patch

from app.clients.identity.identity_client import MockIdentityProvider


@pytest.fixture
def provider():
    return MockIdentityProvider()


def test_disable_user_success(provider):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "success",
            "action": "disable_user",
            "message": "User account disabled."
        }

        result = provider.disable_user("john.doe")

        assert result["status"] == "success"
        assert result["action"] == "disable_user"
        assert result["username"] == "john.doe"
        assert result["message"] == "User account disabled."


def test_disable_user_already_disabled(provider):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "success",
            "action": "disable_user",
            "message": "User account already disabled."
        }

        result = provider.disable_user("john.doe")

        assert result["status"] == "success"
        assert result["message"] == "User account already disabled."


def test_disable_user_not_found(provider):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "failed",
            "action": "disable_user",
            "message": "User not found."
        }

        result = provider.disable_user("john.doe")

        assert result["status"] == "failed"
        assert result["message"] == "User not found."


def test_disable_user_failed(provider):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "failed",
            "action": "disable_user",
            "message": "Unable to disable user account."
        }

        result = provider.disable_user("john.doe")

        assert result["status"] == "failed"
        assert result["message"] == "Unable to disable user account."


def test_revoke_sessions_success(provider):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "success",
            "action": "revoke_sessions",
            "message": "All active sessions revoked."
        }

        result = provider.revoke_sessions("john.doe")

        assert result["status"] == "success"
        assert result["action"] == "revoke_sessions"
        assert result["username"] == "john.doe"
        assert result["message"] == "All active sessions revoked."


def test_revoke_sessions_no_active_sessions(provider):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "success",
            "action": "revoke_sessions",
            "message": "No active sessions found."
        }

        result = provider.revoke_sessions("john.doe")

        assert result["status"] == "success"
        assert result["message"] == "No active sessions found."


def test_revoke_sessions_user_not_found(provider):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "failed",
            "action": "revoke_sessions",
            "message": "User not found."
        }

        result = provider.revoke_sessions("john.doe")

        assert result["status"] == "failed"
        assert result["message"] == "User not found."


def test_revoke_sessions_failed(provider):
    with patch("random.choice") as mock_choice:
        mock_choice.return_value = {
            "status": "failed",
            "action": "revoke_sessions",
            "message": "Unable to revoke active sessions."
        }

        result = provider.revoke_sessions("john.doe")

        assert result["status"] == "failed"
        assert result["message"] == "Unable to revoke active sessions."