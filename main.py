from telegram.ext import ApplicationBuilder, CommandHandler, filters, MessageHandler
from modules.commands import start, help, new_course, add_course, get_courses,delete_course
from modules.config import BOT_TOKEN, seed
import requests

def main():
  seed()
  
  app = ApplicationBuilder().token(BOT_TOKEN).build()  
  app.add_handler(CommandHandler("start", start))
  app.add_handler(CommandHandler("help", help))
  app.add_handler(CommandHandler("get_courses", get_courses))
  app.add_handler(CommandHandler("new_course", new_course))
  app.add_handler(CommandHandler("delete_course", delete_course))
  app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, add_course))

  print("Running Bot")
  app.run_polling()


if __name__ == "__main__":
  main()