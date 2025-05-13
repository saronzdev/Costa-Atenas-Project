from telegram import Update
from telegram.ext import ContextTypes
from modules import config
import requests

async def get_courses(update: Update, context: ContextTypes.DEFAULT_TYPE):
  response = requests.get(config.API_URL)
  if response.status_code == 404: return await update.message.reply_text("No hay cursos") 
  courses = response.json()
  for course in courses:
    result = f"ID: {course["id"]}\nNombre: {course["name"]}\nPrecio: {course["price"]}"
    await update.message.reply_text(result)