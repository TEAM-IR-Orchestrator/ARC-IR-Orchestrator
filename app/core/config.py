from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Automated Ransomware Containment & Incident Response Orchestrator"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Wazuh API Configuration
    WAZUH_API_URL: str
    WAZUH_USERNAME: str
    WAZUH_PASSWORD: str
    WAZUH_VERIFY_SSL: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()