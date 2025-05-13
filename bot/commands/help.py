from telegram import Update
from telegram.ext import ContextTypes
from modules import config

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("\n".join(config.DESCRIPTIONS))