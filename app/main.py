from fastapi import FastAPI

from app.api.routes.webhook import router as webhook_router
from app.core.config import settings
from app.core.logger import configure_logging

# Configure application logging before the app starts
configure_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(webhook_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": f"{settings.APP_NAME} is running.",
    }