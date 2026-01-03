from pydantic import BaseModel
from app.config import settings

class HealthResponse(BaseModel):
    """ Health check response """
    status: str
    service: str
    version: str = settings.version
