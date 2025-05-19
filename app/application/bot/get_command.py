from telegram import Update
from telegram.ext import ContextTypes
from app.infrastructure.api import api_courses

async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  args = context.args
  
  if args:
    try: id = int(" ".join(args))
    except ValueError: return await update.message.reply_text("ID invalido. Intente otra vez")
    response = api_courses.get_one(id)
  else: response = api_courses.get_all()
  
  if "error" in response: response = response["error"].split(":")[0]
  await update.message.reply_text(response)