from telegram import Update
from telegram.ext import ContextTypes
from modules import config
import requests

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  name = update.effective_user.first_name
  await update.message.reply_text(f"Hola {name}, bienvenido/a al bot, usa /help para ver los comandos disponibles")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("\n".join(config.DESCRIPTIONS))

async def new_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = update.effective_user.id
  config.wait[user_id] = True
  await update.message.reply_text("Introduzca el nombre y el precio separados por coma")
  
async def get_courses(update: Update, context: ContextTypes.DEFAULT_TYPE):
  response = requests.get(config.API_URL)
  courses = response.json()
  if len(courses) > 0: 
    for course in courses:
      await update.message.reply_text(course)
  else: await update.message.reply_text("No hay cursos")

async def add_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = update.effective_user.id
  if not config.wait.get(user_id): return
  data = update.message.text.split(",")
  if len(data) < 2:
    return await update.message.reply_text("Formato incorrecto. Intente otra vez")
  name = data[0]
  try: 
    price = float(data[1])
  except ValueError:
    return await update.message.reply_text("Precio incorrecto. Intente otra vez.");
  
  new_course = {"name": name, "price": price}
  response = requests.post(
    config.API_URL,
    json=new_course,
    headers={"Content-Type": "application/json"},
  )
  res = "Añadido" if response.status_code == 201 else "Ha ocurrido un error del lado del servidor"
  config.wait[user_id] = False
  await update.message.reply_text(res)

async def delete_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
  args = context.args
  if not args: return await update.message.reply_text("Ingresa el ID despues del comando para borrar el curso")
  try:
    id = int(" ".join(args))
  except:
    return await update.message.reply_text("ID invalido. Intente otra vez")

  response = requests.delete(f"{config.API_URL}{id}")
  res = "Eliminado" if response.status_code == 200 else "Ha ocurrido un error del lado del servidor"
  await update.message.reply_text(res)