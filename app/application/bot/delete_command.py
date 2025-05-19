from telegram import Update
from telegram.ext import ContextTypes
from app.infrastructure.api import api_courses

async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  args = context.args
  if not args: return await update.message.reply_text("Ingresa el ID despues del comando")
  
  try: id = int(" ".join(args))
  except: return await update.message.reply_text("ID invalido. Intente otra vez")
  
  response = api_courses.delete(id)

  if "error" in response: response = response["error"].split(":")[0]
  await update.message.reply_text(response)