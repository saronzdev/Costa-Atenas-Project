from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 
from backend.modules import config

router = APIRouter()

templates = Jinja2Templates(directory=config.TEMPLATES_DIR)

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@router.get("/courses", response_class=HTMLResponse)
async def courses(request: Request):
  return templates.TemplateResponse("courses.html", {"request": request})