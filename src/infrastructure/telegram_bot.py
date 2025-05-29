import asyncio
import config
from telegram.ext import (
  Application, ApplicationBuilder, CommandHandler, filters, MessageHandler
)
from src.application.courses import CourseServices
from src.infrastructure.database.courses import CoursesRepository
from src.infrastructure.bot.user_state_memory import InMemoryUserState
from src.infrastructure.bot.commands import CommandsHandler
from src.shared.utils import create_bot_commands

def build_bot():
  repo = CoursesRepository(config.DB_DIR)
  services = CourseServices(repo)
  user_state = InMemoryUserState()
  commands = CommandsHandler(services, user_state)

  
  app = ApplicationBuilder() \
    .token(config.BOT_TOKEN) \
    .post_init(lambda application: application.bot.set_my_commands(create_bot_commands())) \
    .build()

  command_map = {
    "start": commands.start,
    "help": commands.help,
    "get": commands.get,
    "new": commands.new,
    "delete": commands.delete,
    "update": commands.update,
  }
  
  for cmd, handler in command_map.items():
    app.add_handler(CommandHandler(cmd, handler))

  app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, commands.handler_inputs))
  return app

def start_telegram_bot():
  print("Running Bot")
  app = build_bot()
  asyncio.run(app.run_polling())
  
if __name__ == "__main__":
  start_telegram_bot()