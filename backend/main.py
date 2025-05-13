from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.modules import config
from backend.routes import courses_routes, html_routes
from backend.db import init_db

init_db.init()

app = FastAPI()

app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")

app.include_router(html_routes.router, prefix="")
app.include_router(courses_routes.router, prefix="/api/courses")