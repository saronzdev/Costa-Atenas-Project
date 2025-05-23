from telegram.ext import Application, ApplicationBuilder, CommandHandler, filters, MessageHandler
from src.application.bot_commands import TelegramCommandHandler
from src.shared.utils import create_bot_commands
import config
import asyncio

commands = TelegramCommandHandler()

async def post_init(application: Application):
  await application.bot.set_my_commands(create_bot_commands())

app = ApplicationBuilder().token(config.BOT_TOKEN).post_init(post_init).build()  
app.add_handler(CommandHandler("start", commands.start))
app.add_handler(CommandHandler("help", commands.help))
app.add_handler(CommandHandler("get", commands.get))
app.add_handler(CommandHandler("new", commands.new))
app.add_handler(CommandHandler("delete", commands.delete))
app.add_handler(CommandHandler("update", commands.update))
  
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, commands.handler_inputs))

def start_telegram_bot():
  print("Running Bot")
  asyncio.run(app.run_polling())
  
if __name__ == "__main__":
  start_telegram_bot()