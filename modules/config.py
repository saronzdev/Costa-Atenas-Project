import os
from pathlib import Path
from telegram import BotCommand
from dotenv import load_dotenv

load_dotenv()

DB_PATH = Path(__file__).parent.parent / "db.json"
BOT_TOKEN = os.getenv("BOT_TOKEN") 
API_URL = "localhost:3000/data"
COMMANDS = [
  BotCommand("start", "Iniciar el bot"),
  BotCommand("help", "Mostrar los comandos disponibles"),
  BotCommand("new_course", "Añadir nuevo curso"),
  BotCommand("get_courses", "Obtener cursos disponibles"),
  BotCommand("delete_course", "Borrar un curso")
]

DESCRIPTIONS = [
  "Usa /start para inicar (o reiniciar) el bot",
  "Usa /help para ver más información de los commandos",
  "Usa /new_course para añadir nuevo un curso",
  "Usa /get_courses para mostart una lista de los cursos disponibles",
  "Usa /delete_course <ID> para borrar el curso con dicho ID"
]

def seed():
  if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
      f.write("[]") 