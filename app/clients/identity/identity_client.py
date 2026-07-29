import random


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

        # Predefined mock responses for disabling a user account.
        responses = [
            {
                "status": "success",
                "action": "disable_user",
                "message": "User account disabled."
            },
            {
                "status": "success",
                "action": "disable_user",
                "message": "User account already disabled."
            },
            {
                "status": "failed",
                "action": "disable_user",
                "message": "User not found."
            },
            {
                "status": "failed",
                "action": "disable_user",
                "message": "Unable to disable user account."
            }
        ]

        response = random.choice(responses)

        return {
            "status": response["status"],
            "action": response["action"],
            "username": username,
            "message": response["message"]
        }

    def revoke_sessions(self, username: str):
        """
        Simulate revoking all active sessions
        for a compromised user.
        """

        # Predefined mock responses for revoking user sessions.
        responses = [
            {
                "status": "success",
                "action": "revoke_sessions",
                "message": "All active sessions revoked."
            },
            {
                "status": "success",
                "action": "revoke_sessions",
                "message": "No active sessions found."
            },
            {
                "status": "failed",
                "action": "revoke_sessions",
                "message": "User not found."
            },
            {
                "status": "failed",
                "action": "revoke_sessions",
                "message": "Unable to revoke active sessions."
            }
        ]

        response = random.choice(responses)

        return {
            "status": response["status"],
            "action": response["action"],
            "username": username,
            "message": response["message"]
        }
    