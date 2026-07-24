from app.integrations.mock_identity_provider import MockIdentityProvider


class IdentityService:
    """
    Service responsible for identity containment actions.

    Business logic related to user suspension and
    session revocation should live here, while
    communication with the Identity Provider is
    delegated to MockIdentityProvider.
    """

    def __init__(self):
        self.identity_provider = MockIdentityProvider()

    def suspend_user(self, username: str):
        """
        Suspend a compromised user account.
        """
        pass

    def revoke_user_sessions(self, username: str):
        """
        Revoke all active sessions for
        a compromised user.
        """
        pass