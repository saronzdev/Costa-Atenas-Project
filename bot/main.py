from telegram.ext import Application, ApplicationBuilder, CommandHandler, filters, MessageHandler
from modules.commands import start, help, new_course, add_course, get_courses,delete_course
from modules.config import BOT_TOKEN, COMMANDS

async def post_init(application: Application):
  await application.bot.set_my_commands(COMMANDS)

def main():
  app = ApplicationBuilder().token(BOT_TOKEN).post_init(post_init).build()  
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