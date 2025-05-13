from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.modules import config
from backend.routes import courses_routes
from backend.db import init_db

init_db.init()

app = FastAPI()

app.include_router(courses_routes.router, prefix="/api/courses", tags=["Courses"])
app.mount("/", StaticFiles(directory=config.CLIENT_PATH, html=True), name="client")