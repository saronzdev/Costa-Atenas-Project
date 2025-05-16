import os
from telegram import BotCommand
from dotenv import load_dotenv

load_dotenv()

user_states = {}

BOT_TOKEN = os.getenv("BOT_TOKEN") 
API_URL = os.getenv("API_URL") + "/api/courses/"

COMMANDS = [
  BotCommand("start", "Iniciar el bot"),
  BotCommand("help", "Mostrar los comandos disponibles"),
  BotCommand("new_course", "Añadir nuevo curso"),
  BotCommand("get_courses", "<ID opcional> obtener cursos disponibles"),
  BotCommand("delete_course", "Borrar un curso"),
  BotCommand("update_course", "Actualizar un curso")
]

DESCRIPTIONS = [
  "Usa /start para inicar (o reiniciar) el bot",
  "Usa /help para ver más información de los commandos",
  "Usa /new_course para añadir nuevo un curso",
  "Usa /get_courses para mostar una lista de los cursos disponibles (permite búsqueda por ID)",
  "Usa /delete_course <ID> para borrar el curso con dicho ID",
  "Usa /update_course <ID> para actualizar el curso con dicho ID"
]