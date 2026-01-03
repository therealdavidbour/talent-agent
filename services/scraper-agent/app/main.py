from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.models import HealthResponse
import logging

logging.basicConfig(
    level=settings.log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title='Scraper Agent',
    description='Scrapes job listings from job boards',
    version=settings.version
)

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=settings.allow_origins,
    allow_credentials=settings.allow_credentials,
    allow_methods=settings.allow_methods,
    allow_headers=settings.allow_headers
)

@app.get('/health', response_model=HealthResponse)
async def  health_check():
    return HealthResponse(status="healthy", service=settings.service_name)

@app.get('/')
async def root():
    return {
        'service': settings.service_name,
        'status': 'running',
        'docs': '/docs'
    }
