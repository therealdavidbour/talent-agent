from pydantic_settings import BaseSettings
from typing import Optional, List

class Settings(BaseSettings):

    # Service Configuration
    service_name: str = 'scraper-agent'
    service_port: int = 8001
    debug: bool = True
    version: str = "1.0.0"

    # CORS
    allow_origins: List[str] = ["*"]
    allow_methods: List[str] = ["*"]
    allow_headers: List[str] = ["*"]
    allow_credentials: bool = False

    # Browser Settings
    browser_headless: bool = True
    browser_timeout: int = 30000 # in milliseconds
    user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

    # Scraping Settings
    max_jobs_per_request: int = 100
    default_timeout: int = 30
    enable_screenshots: bool = False

    # Anthropic API Key
    anthroptic_api_key: Optional[str] = None

    # Logging
    log_level: str = 'INFO'

settings = Settings()

    
