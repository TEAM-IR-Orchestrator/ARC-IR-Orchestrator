import requests
import urllib3

from app.clients.edr.wazuh_client import WazuhClient

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = WazuhClient()
token = client.authenticate()

url = f"{client.base_url}/active-response?agents_list=001"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

payload = {
    "command": "!firewall-drop",
    "arguments": []
}

response = requests.put(
    url,
    headers=headers,
    json=payload,
    verify=False,
    timeout=30
)

print(response.status_code)
print(response.text)