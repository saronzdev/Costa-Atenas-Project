from telegram import Update
from telegram.ext import ContextTypes
import config

async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = update.effective_user.id
  config.user_states[user_id] = {"state": 1}
  config.user_states[user_id].update({"type": 1})
  await update.message.reply_text("Ingrese el nombre")