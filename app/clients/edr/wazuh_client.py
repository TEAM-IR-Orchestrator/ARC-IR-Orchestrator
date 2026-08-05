import requests
import urllib3

from app.core.config import settings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from app.schemas.parsed_alert import ParsedAlert


class WazuhClient:
    """
    Client responsible for communicating with
    the Wazuh REST API.
    """

    def __init__(self):
        self.base_url = settings.WAZUH_API_URL
        self.username = settings.WAZUH_USERNAME
        self.password = settings.WAZUH_PASSWORD
        self.verify_ssl = settings.WAZUH_VERIFY_SSL

        self.token = None

    def authenticate(self):
        """
        Authenticate with the Wazuh API and
        store the JWT token.
        """

        response = requests.get(
            f"{self.base_url}/security/user/authenticate",
            auth=(self.username, self.password),
            params={"raw": "true"},
            verify=self.verify_ssl,
            timeout=15
        )

        response.raise_for_status()

        self.token = response.text.strip()

        return self.token

    def get_agents(self):
        """
        Retrieve all registered Wazuh agents.
        """
        if self.token is None:
            self.authenticate()

        response = requests.get(
            f"{self.base_url}/agents",
            headers={
                "Authorization": f"Bearer {self.token}"
            },
            verify=self.verify_ssl,
            timeout=15
        )

        response.raise_for_status()

        return response.json()

    def find_agent_by_hostname(self, hostname: str):
        """
        Find a Wazuh agent by its hostname.
        """

        agents = self.get_agents()

        for agent in agents["data"]["affected_items"]:
            if agent["name"].lower() == hostname.lower():
                return agent

        return None

    def isolate_host(
        self,
        agent_id: str,
        alert: ParsedAlert,
    ):
        """
        Trigger Wazuh Active Response to isolate an endpoint.
        """

        if self.token is None:
            self.authenticate()

        url = (
            f"{self.base_url}/active-response"
            f"?agents_list={agent_id}"
        )

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        payload = {
            "command": "!orchestrator-isolate",
            "arguments": [],
            "alert": {
                "rule": {
                    "id": alert.rule_id,
                    "level": alert.rule_level,
                    "description": alert.title,
                    "groups": alert.groups,
                    "mitre": {
                        "id": alert.mitre_id,
                        "technique": alert.mitre_technique,
                        "tactic": alert.mitre_tactic,
                    },
                },
                "agent": {
                    "id": alert.device_id,
                    "name": alert.hostname,
                    "ip": alert.ip_address,
                },
                "data": alert.event_data,
                "full_log": alert.description,
            },
        }

        print("========== ACTIVE RESPONSE REQUEST ==========")
        print("URL:", url)
        print("PAYLOAD:", payload)
        print("============================================")

        response = requests.put(
            url,
            headers=headers,
            json=payload,
            verify=self.verify_ssl,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()