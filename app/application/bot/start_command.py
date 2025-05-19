from telegram import Update
from telegram.ext import ContextTypes

async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  name = update.effective_user.first_name
  await update.message.reply_text(f"Hola {name}, bienvenido/a al bot, usa /help para ver los comandos disponibles")