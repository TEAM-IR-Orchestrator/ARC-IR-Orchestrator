from app.schemas.parsed_alert import ParsedAlert


class AlertParser:
    """
    Converts vendor-specific webhook payloads
    into a standardized ParsedAlert object.
    """

    def parse(self, alert_data: dict, provider: str) -> ParsedAlert:
        provider = provider.upper()

        if provider == "MANUAL":
            return self._parse_manual(alert_data)

        elif provider == "CROWDSTRIKE":
            return self._parse_crowdstrike(alert_data)

        raise ValueError(f"Unsupported provider: {provider}")
    
    def _parse_manual(self, alert_data: dict) -> ParsedAlert:
        return ParsedAlert(
            alert_id=alert_data["alert_id"],
            provider="MANUAL",
            severity=alert_data["severity"],
            timestamp=alert_data["timestamp"],

            hostname=alert_data["hostname"],
            ip_address=alert_data["ip_address"],
            device_id=alert_data.get("device_id"),

            username=alert_data["username"],

            process_name=alert_data["process_name"],
            process_hash=alert_data["process_hash"],

            title=alert_data.get("title"),
            description=alert_data.get("description"),
            )
    
    def _parse_crowdstrike(self, alert_data: dict) -> ParsedAlert:
        return ParsedAlert(
            alert_id=alert_data["alert_id"],
            provider="CROWDSTRIKE",
            severity=alert_data["severity"],
            timestamp=alert_data["timestamp"],

            hostname=alert_data["hostname"],
            ip_address=alert_data["ip_address"],
            device_id=alert_data.get("device_id"),

            username=alert_data["username"],

            process_name=alert_data["process_name"],
            process_hash=alert_data["process_hash"],
            title=alert_data.get("title"),
            description=alert_data.get("description"),
        )