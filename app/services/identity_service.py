from app.clients.identity.identity_client import MockIdentityProvider
from app.core.logger import get_logger

logger = get_logger(__name__)


class IdentityService:
    """
    Service responsible for identity containment actions.

    Business logic related to user suspension and
    session revocation lives here, while communication
    with the identity provider is delegated to the client.
    """

    def __init__(self):
        self.identity_provider = MockIdentityProvider()

    def suspend_user(self, username: str):
        logger.info(
            "Suspending user '%s'.",
            username,
        )

        response = self.identity_provider.disable_user(username)
        logger.info(
            "User suspension result: %s",
            response,
        )

        return response

    def revoke_user_sessions(self, username: str):
        logger.info(
            "Revoking active sessions for user '%s'.",
            username,
        )

        response = self.identity_provider.revoke_sessions(username)

        logger.info(
            "Session revocation result: %s",
            response,
        )

        return response