from telegram.ext import Application, ApplicationBuilder, CommandHandler, filters, MessageHandler
from app.application.bot import start_command, help_command, get_command, new_command, update_command, delete_command, handler_inputs
from config import create_bot_commands
import config
import asyncio

async def post_init(application: Application):
  await application.bot.set_my_commands(create_bot_commands())

app = ApplicationBuilder().token(config.BOT_TOKEN).post_init(post_init).build()  
app.add_handler(CommandHandler("start", start_command.command))
app.add_handler(CommandHandler("help", help_command.command))
app.add_handler(CommandHandler("get", get_command.command))
app.add_handler(CommandHandler("new", new_command.command))
app.add_handler(CommandHandler("delete", delete_command.command))
app.add_handler(CommandHandler("update", update_command.command))
  
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler_inputs.handler))

def start_telegram_bot():
  print("Running Bot")
  asyncio.run(app.run_polling())
  
if __name__ == "__main__":
  start_telegram_bot()