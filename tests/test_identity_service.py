import pytest
from unittest.mock import MagicMock

from app.services.identity_service import IdentityService


@pytest.fixture
def service():
    return IdentityService()


def test_suspend_user_calls_provider(service):
    expected = {
        "status": "success",
        "action": "disable_user",
        "username": "john.doe",
        "message": "User account disabled."
    }

    service.identity_provider.disable_user = MagicMock(return_value=expected)

    result = service.suspend_user("john.doe")

    service.identity_provider.disable_user.assert_called_once_with("john.doe")
    assert result == expected


def test_revoke_sessions_calls_provider(service):
    expected = {
        "status": "success",
        "action": "revoke_sessions",
        "username": "john.doe",
        "message": "All active sessions revoked."
    }

    service.identity_provider.revoke_sessions = MagicMock(return_value=expected)

    result = service.revoke_user_sessions("john.doe")

    service.identity_provider.revoke_sessions.assert_called_once_with("john.doe")
    assert result == expected