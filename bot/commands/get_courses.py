from telegram import Update
from telegram.ext import ContextTypes
from api import get

async def get_courses(update: Update, context: ContextTypes.DEFAULT_TYPE):
  args = context.args
  if args:
    try: id = int(" ".join(args))
    except ValueError: return await update.message.reply_text("ID invalido. Intente otra vez")
    result = await get.get_one(id)
  else: result = await get.get_all()
  
  await update.message.reply_text(result)