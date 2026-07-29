from app.clients.evidence.evidence_client import MockLiveResponseClient


class EvidenceCollectionService:
    """
    Service responsible for coordinating
    forensic evidence collection.

    Business logic related to evidence collection
    belongs here, while remote execution is
    delegated to the MockLiveResponseClient.
    """

    def __init__(self):
        self.live_response_client = MockLiveResponseClient()

    def collect_kape(self, hostname: str):
        """
        Execute remote KAPE acquisition.
        """
        response = self.live_response_client.execute_kape(hostname)
        return response

    def capture_ram(self, hostname: str):
        """
        Execute remote memory acquisition.
        """
        response = self.live_response_client.capture_memory(hostname)
        return response