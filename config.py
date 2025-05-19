import os
from telegram import BotCommand
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

def create_bot_commands():
  COMMANDS = [
    BotCommand("start", "Iniciar el bot"),
    BotCommand("help", "Mostrar los comandos disponibles"),
    BotCommand("new", "Añadir nuevo curso"),
    BotCommand("get", "<ID opcional> obtener cursos disponibles"),
    BotCommand("delete", "Borrar un curso"),
    BotCommand("update", "Actualizar un curso")
  ]
  return COMMANDS