from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from modules import config
from routes import courses_routes

config.seed_db()
app = FastAPI()

app.include_router(courses_routes.router, prefix="/api/courses", tags=["Courses"])
app.mount("/", StaticFiles(directory=config.CLIENT_PATH, html=True), name="client")