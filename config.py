import os
from dotenv import load_dotenv

load_dotenv()

user_states = {}

BOT_TOKEN = os.getenv("BOT_TOKEN")
BACKEND_URL =  os.getenv("API_URL")
API_URL = BACKEND_URL + "api/courses/"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(ROOT_DIR, "app")

DB_DIR = os.path.join(ROOT_DIR, "database.db")
STATIC_DIR = os.path.join(BASE_DIR, "infrastructure", "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "infrastructure", "templates")