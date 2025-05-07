from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from .config import DB_PATH
import json

wait = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("Usa /help para ayuda")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text(
    """
    Usa /new_course <ID> para añadir un curso
  """)

async def new_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = update.effective_user.id
  wait[user_id] = True
  await update.message.reply_text("Introduzca el nombre y el precio separados por coma")
  

async def get_courses(update: Update, context: ContextTypes.DEFAULT_TYPE):
  with open(DB_PATH, "r") as f:
    courses = json.load(f)
  
  if len(courses) > 0:
    for course in courses:
      response = f"ID: {course["id"]}\nNombre: {course["name"]}\nPrecio: {course["price"]}"
      await update.message.reply_text(response)      
  else:  
    await update.message.reply_text("No hay datos") 

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
  with open(DB_PATH, "r") as f:
    db = json.load(f)
    id = len(db) + 1
    data_to_save = {"id": id, "name": name, "price": price}
    db.append(data_to_save)
  
  with open(DB_PATH, "w") as f:
    json.dump(db, f)

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
  


  
  