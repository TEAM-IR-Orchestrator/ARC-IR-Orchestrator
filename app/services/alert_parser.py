from app.schemas.parsed_alert import ParsedAlert


class AlertParser:
    """
    Converts Wazuh webhook payloads into a standardized ParsedAlert object.
    """

    def parse(self, alert_data: dict, provider: str) -> ParsedAlert:
        provider = provider.upper()

        if provider == "WAZUH":
            return self._parse_wazuh(alert_data)

        raise ValueError(f"Unsupported provider: {provider}")

    def _convert_wazuh_severity(self, level: int) -> str:
        """
        Convert Wazuh rule levels into internal severity levels.
        """

        if level <= 2:
            return "Low"
        elif level <= 7:
            return "Medium"
        elif level <= 11:
            return "High"
        else:
            return "Critical"

    def _parse_wazuh(self, alert_data: dict) -> ParsedAlert:

        rule = alert_data.get("rule", {})
        agent = alert_data.get("agent", {})
        data = alert_data.get("data", {})
        mitre = rule.get("mitre", {})
        

        return ParsedAlert(

            # Alert Information
            alert_id=alert_data.get("id", ""),
            provider="WAZUH",
            severity=self._convert_wazuh_severity(rule.get("level", 0)),
            rule_level=rule.get("level", 0),
            rule_id=rule.get("id", ""),
            timestamp=alert_data.get("@timestamp"),

            # Device Information
            hostname=agent.get("name", ""),
            ip_address=agent.get("ip", ""),
            device_id=agent.get("id"),
            source_ip=alert_data.get("data", {}).get("srcip"),

            # User Information
            username=data.get("srcuser")
            or data.get("dstuser")
            or "",

            # Process Information
            process_name=data.get("process_name"),
            process_hash=data.get("process_hash"),

            # Alert Details
            title=rule.get("description"),
            description=alert_data.get("full_log"),

            # Wazuh Information
            groups=rule.get("groups", []),
            mitre_id=mitre.get("id", []),
            mitre_technique=mitre.get("technique", []),
            mitre_tactic=mitre.get("tactic", []),

            # Raw Event Data
            event_data=data,
        )