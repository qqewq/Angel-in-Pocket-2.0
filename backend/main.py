from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.api.routes import api_router
from config.settings import settings
import uvicorn

app = FastAPI(title="Angel-in-Pocket 2.0")
app.mount("/dashboard", StaticFiles(directory="frontend", html=True), name="frontend")
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host=settings.host, port=settings.port, reload=True)
