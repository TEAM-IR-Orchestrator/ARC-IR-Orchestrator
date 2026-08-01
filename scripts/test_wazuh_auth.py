from app.clients.edr.wazuh_client import WazuhClient

client = WazuhClient()

agent = client.find_agent_by_hostname("Ubuntu-desktop")

print(agent)