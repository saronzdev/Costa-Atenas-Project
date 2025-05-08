from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from .config import API_URL, DESCRIPTIONS
import json
import requests

wait = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  name = update.effective_user.first_name
  await update.message.reply_text(f"Hola {name}, bienvenido/a al bot, usa /help para ver los comandos disponibles")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("\n".join(DESCRIPTIONS))

async def new_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = update.effective_user.id
  wait[user_id] = True
  await update.message.reply_text("Introduzca el nombre y el precio separados por coma")
  

async def get_courses(update: Update, context: ContextTypes.DEFAULT_TYPE):
  response = requests.get(API_URL)
  courses = response.json()
  if len(courses) > 0: 
    for course in courses:
      await update.message.reply_text(course)
  else: await update.message.reply_text("No hay cursos")

async def add_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = update.effective_user.id
  if not wait.get(user_id): return
  data = update.message.text.split(",")
  if len(data) < 2:
    return await update.message.reply_text("Formato incorrecto. Intente otra vez")
  name = data[0]
  
  try: 
    price = float(data[1])
  except ValueError:
    return await update.message.reply_text("Precio incorrecto. Intente otra vez.");
  
  wait[user_id] = False
  new_course = {"name": name, "price": price}
  response = requests.post(
    API_URL,
    json=new_course,
    headers = {"Content-Type": "application/json"},
  )

  await update.message.reply_text("Añadido a la BD")

async def delete_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
  args = context.args
  if not args: return await update.message.reply_text("Ingresa el ID despues del comando para borrar el curso")
  try:
    id = int(" ".join(args))
  except:
    return await update.message.reply_text("ID invalido. Intente otra vez")
  
  with open(DB_PATH, "r") as f:
    courses = json.load(f)
    found = False
    if len(courses) > 0:
      for index, course in enumerate(courses):
        if int(course["id"]) == id:
          courses.pop(index)
          found = True
  
  if not found: return await update.message.reply_text("El curso no existe")

  with open(DB_PATH, "w") as f:
    json.dump(courses, f)
  return await update.message.reply_text("El curso fue eliminado")
  


  
  