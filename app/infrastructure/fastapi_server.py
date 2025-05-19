from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.application.endpoints import courses
import config
import uvicorn
from app.application.endpoints import html, courses
from app.infrastructure.database.db import init_db

init_db()

app = FastAPI()
app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")
app.include_router(html.router, prefix="")
app.include_router(courses.router, prefix="/api/courses")

def start_fastapi_server():
  uvicorn.run(app, host="127.0.0.1", port=3000, log_level="info")