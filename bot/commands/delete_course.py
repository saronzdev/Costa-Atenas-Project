from telegram import Update
from telegram.ext import ContextTypes
from api import delete

async def delete_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
  args = context.args
  if not args: return await update.message.reply_text("Ingresa el ID despues del comando")
  
  try: id = int(" ".join(args))
  except: return await update.message.reply_text("ID invalido. Intente otra vez")
  
  response = await delete.delete(id)

  await update.message.reply_text(response)