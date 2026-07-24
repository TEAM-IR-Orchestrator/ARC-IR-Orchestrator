class MockIdentityProvider:
    """
    Mock Identity Provider client.

    This class simulates an enterprise Identity Provider
    such as Microsoft Entra ID (Azure AD), Okta,
    or Active Directory.

    It is responsible only for simulating identity
    operations. Business logic should not exist here.
    """

    def disable_user(self, username: str):
        """
        Simulate disabling a compromised user account.
        """
        pass

    def revoke_sessions(self, username: str):
        """
        Simulate revoking all active sessions
        for a compromised user.
        """
        pass