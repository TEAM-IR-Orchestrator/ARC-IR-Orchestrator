from app.clients.edr.wazuh_client import WazuhClient


def main():

    client = WazuhClient()

    response = client.isolate_host(
        agent_id="001",
    )

    print(response)


if __name__ == "__main__":
    main()