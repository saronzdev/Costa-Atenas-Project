from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.infrastructure.routes import courses, web_page
import config
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")
app.include_router(web_page.router, prefix="")
app.include_router(courses.router, prefix="/api/courses")

def start_fastapi_server():
  uvicorn.run(app, host="127.0.0.1", port=3000, log_level="info")