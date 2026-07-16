from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.webhook import router as webhook_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)
app.include_router(webhook_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": f"{settings.APP_NAME} is running."
    }