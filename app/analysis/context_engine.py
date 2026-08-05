from app.schemas.parsed_alert import ParsedAlert
from app.models.engine_result import EngineResult

class ContextEngine:
    """
    Evaluates the environment surrounding an alert rather than
    the alert itself.

    This engine helps reduce false positives by considering
    asset importance and operational context.
    """

    # Critical assets in the environment
    CRITICAL_HOSTS = {
        "domain-controller",
        "dc01",
        "dc02",
        "fileserver",
        "database",
        "backup-server",
    }

    # High-value accounts
    PRIVILEGED_USERS = {
        "administrator",
        "admin",
        "root",
        "domainadmin",
    }

    def evaluate(self, alert: ParsedAlert):

        score = 0
        reasons = []

        # Critical Host
        if alert.hostname.lower() in self.CRITICAL_HOSTS:
            score += 30
            reasons.append(
                f"Critical asset detected ({alert.hostname}) (+30)"
            )

        # Privileged Account
        if alert.username:

            if alert.username.lower() in self.PRIVILEGED_USERS:
                score += 25
                reasons.append(
                    f"Privileged account involved ({alert.username}) (+25)"
                )

        return EngineResult(
            score=score,
            reasons=reasons,
        )