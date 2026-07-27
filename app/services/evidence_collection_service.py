from app.integrations.mock_live_response_client import MockLiveResponseClient


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
        pass

    def capture_ram(self, hostname: str):
        """
        Execute remote memory acquisition.
        """
        pass