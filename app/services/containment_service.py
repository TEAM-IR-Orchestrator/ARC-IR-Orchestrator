from app.clients.edr.wazuh_client import WazuhClient
from app.core.logger import get_logger
from app.schemas.parsed_alert import ParsedAlert

logger = get_logger(__name__)


class ContainmentService:
    """
    Executes endpoint containment by delegating
    to the configured EDR client.
    """

    def __init__(self):
        self.edr_client = WazuhClient()

    def contain_host(self, agent_id: str, hostname: str, alert: ParsedAlert,):
        if not agent_id:
            raise ValueError(
            f"No Wazuh agent ID available for host '{hostname}'."
        )

        logger.info(
            "Starting containment for host '%s'.",
            hostname,
        )

        result = self.edr_client.isolate_host(agent_id = agent_id, alert=alert)

        status = str(result.get("status", "")).lower()
        message = str(result.get("message", "")).lower()

        if status == "success":

            if "already" in message:

                logger.info(
                    "Host '%s' is already isolated.",
                    hostname,
                )

            else:

                logger.info(
                    "Host '%s' isolated successfully.",
                    hostname,
                )

        elif status == "failed":

            logger.error(
                "Containment failed for host '%s': %s",
                hostname,
                result.get("message"),
            )

        else:

            logger.warning(
                "Unexpected containment response: %s",
                result,
            )

        return result