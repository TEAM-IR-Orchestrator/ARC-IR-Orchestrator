import requests
import urllib3

from app.core.config import settings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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

    def isolate_host(self, agent_id: str):
        """
        Trigger containment on a Wazuh agent.

        TODO:
        Implement using the Wazuh Active Response API.
        """
        pass