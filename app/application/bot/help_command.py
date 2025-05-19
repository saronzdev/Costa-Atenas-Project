from telegram import Update
from telegram.ext import ContextTypes
from app.domain.services import get_commands_desc

async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("\n".join(get_commands_desc()))