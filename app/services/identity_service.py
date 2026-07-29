from app.clients.identity.identity_client import MockIdentityProvider


class IdentityService:
    """
    Service responsible for identity containment actions.

    Business logic related to user suspension and
    session revocation should live here, while
    communication with the Identity Provider is
    delegated to MockIdentityProvider.
    """

    def __init__(self):
     """Initialize the identity provider client."""
     self.identity_provider = MockIdentityProvider()

    # Disable the specified user account.
    def suspend_user(self, username: str):
        response = self.identity_provider.disable_user(username)
        return response

    def revoke_user_sessions(self, username: str):
        """
        Revoke all active sessions for
        a compromised user.
        """
        response = self.identity_provider.revoke_sessions(username)
        return response