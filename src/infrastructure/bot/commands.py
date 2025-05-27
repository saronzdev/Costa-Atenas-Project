from telegram import Update
from telegram.ext import ContextTypes
from src.domain.bot_handler import BotCommandHandler
from src.shared import schemas, utils
from src.application.courses import CourseServices
from src.infrastructure.database.courses import CoursesRepository
from src.shared.exceptions import try_except
import config

repo = CoursesRepository(config.DB_DIR)
courses = CourseServices(repo)

class CommandsHandler(BotCommandHandler):
  async def start_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text(f"Hola {name}, bienvenido/a al bot, usa /help para ver los comandos disponibles")

  async def help_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("\n".join(utils.get_commands()))

  async def get_courses_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    if args:
      try: id = int(" ".join(args))
      except ValueError: return await update.message.reply_text("ID invalido. Intente otra vez")
      response = courses.get_one(id, formated=True)
    else: response = courses.get_all(formated=True)

    if "error" in response: response = try_except(response["error"])
    await update.message.reply_text(response)

  async def new_course_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    config.user_states[user_id] = {"state": 1}
    config.user_states[user_id].update({"type": 1})
    await update.message.reply_text("Ingrese el nombre")

  async def update_course_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args
    if not args: return await update.message.reply_text("Ingresa el ID despues del comando")
    try: id = int(" ".join(args))
    except: return await update.message.reply_text("ID invalido. Intente otra vez")
    
    data = courses.get_one(id)
    if "error" in data: return await update.message.reply_text(try_except(data["error"]))
    
    config.user_states[user_id] = {"state": 1}
    config.user_states[user_id].update({"type": 2})
    config.user_states[user_id].update({"id": id})

    await update.message.reply_text('Ingre el nuevo nombre ("-" para dejar el original)')

  async def delete_course_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args: return await update.message.reply_text("Ingresa el ID despues del comando")

    try: id = int(" ".join(args))
    except: return await update.message.reply_text("ID invalido. Intente otra vez")

    response = courses.delete_one(id)
    if "error" in response: response = try_except(response["error"])
    else: response = "Borrado"
    await update.message.reply_text(response)

  async def handler_inputs_cmd(self, update, context):
    user_id = update.effective_user.id
    message = update.message.text.strip()

    if user_id not in config.user_states: return

    type = config.user_states[user_id]["type"]
    state = config.user_states[user_id]["state"]

    text_price = 'Ingre el nuevo precio ("-" para dejar el original)' if type == 2 else "Ingrese el precio"

    if state == 1:
      config.user_states[user_id]["name"] = message
      config.user_states[user_id]["state"] = 2
      await update.message.reply_text(text_price)

    elif state == 2:
      config.user_states[user_id]["price"] = message
      name = config.user_states[user_id]["name"]
      price = config.user_states[user_id]["price"]

      if price.strip() != "-":
        try: price = float(price)
        except: return await update.message.reply_text("Precio incorrecto. Intente otra vez.")
      else: price = None

      if name.strip() == "-": name = None
      data = schemas.CourseUpdate(name=name, price=price)

      if type == 1:
        response = courses.save(data)
      elif type == 2:
        id = config.user_states[user_id]["id"]
        response = courses.update_one(id, data)

      del config.user_states[user_id]

      if "error" in response: response = try_except(response["error"])
      else: response = "Hecho"
      await update.message.reply_text(response)
