"""
Application settings and configuration.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Runtime settings loaded from environment variables.

    Attributes:
        app_name: Public application name.
        owner_email: Default notification email for new leads.
        formspree_endpoint: Formspree endpoint URL for lead submissions.
        gallery_directory: Absolute or relative gallery image directory.
        environment: Runtime environment label.
    """

    app_name: str = "For Shor"
    owner_email: str = "owner@forshor.local"
    formspree_endpoint: str = ""
    gallery_directory: str = "src/forshor/static/images/gallery"
    environment: str = "development"

    model_config = SettingsConfigDict(env_prefix="FORSHOR_")


settings = Settings()
