from telegram import Update
from telegram.ext import ContextTypes
from modules import config

async def update_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = update.effective_user.id
  args = context.args
  if not args: return await update.message.reply_text("Ingresa el ID despues del comando")
  try: id = int(" ".join(args))
  except: return await update.message.reply_text("ID invalido. Intente otra vez")
  config.user_states[user_id] = {"state": 1}
  config.user_states[user_id].update({"type": 2})
  config.user_states[user_id].update({"id": id})

  await update.message.reply_text('Ingre el nuevo nombre ("-" para dejar el original)')