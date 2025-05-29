from telegram import Update
from telegram.ext import ContextTypes
from src.domain.bot_handler import BotCommandHandler
from src.shared import schemas, utils
from src.shared.exceptions import try_except

class CommandsHandler(BotCommandHandler):
  def __init__(self, course_services, user_state_manager):
    self.courses = course_services
    self.user_state = user_state_manager

  async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text(
      f"Hola {name}, bienvenido/a al bot, usa /help para ver los comandos disponibles"
    )

  async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("\n".join(utils.get_commands()))

  async def get(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if args:
      try:
        course_id = int(" ".join(args))
        response = self.courses.get_one(course_id, formated=True)
      except ValueError:
        return await update.message.reply_text("ID invalido. Intente otra vez")
    else:
      response = self.courses.get_all(formated=True)

    if "error" in response:
      response = try_except(response["error"])
    await update.message.reply_text(response)

  async def new(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    self.user_state.set(user_id, {"state": 1, "type": 1})
    await update.message.reply_text("Ingrese el nombre")

  async def update(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args
    if not args:
      return await update.message.reply_text("Ingresa el ID despues del comando")
    try:
      course_id = int(" ".join(args))
    except ValueError:
      return await update.message.reply_text("ID invalido. Intente otra vez")

    data = self.courses.get_one(course_id)
    if "error" in data:
      return await update.message.reply_text(try_except(data["error"]))

    self.user_state.set(user_id, {"state": 1, "type": 2, "id": course_id})
    await update.message.reply_text('Ingre el nuevo nombre ("-" para dejar el original)')

  async def delete(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
      return await update.message.reply_text("Ingresa el ID despues del comando")
    try:
      course_id = int(" ".join(args))
    except ValueError:
      return await update.message.reply_text("ID invalido. Intente otra vez")

    response = self.courses.delete_one(course_id)
    if "error" in response:
      response = try_except(response["error"])
    else:
      response = "Borrado"
    await update.message.reply_text(response)

  async def handler_inputs(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.message.text.strip()

    if not self.user_state.has(user_id):
      return

    state_data = self.user_state.get(user_id)
    op_type = state_data["type"]
    state = state_data["state"]

    text_price = (
      'Ingre el nuevo precio ("-" para dejar el original)'
      if op_type == 2 else "Ingrese el precio"
    )

    if state == 1:
      state_data["name"] = message
      state_data["state"] = 2
      self.user_state.set(user_id, state_data)
      await update.message.reply_text(text_price)
      return

    if state == 2:
      state_data["price"] = message
      name = state_data["name"]
      price = state_data["price"]

      if price.strip() != "-":
        try:
          price = float(price)
        except ValueError:
          return await update.message.reply_text("Precio incorrecto. Intente otra vez.")
      else:
        price = None

      if name.strip() == "-":
        name = None
      data = schemas.CourseUpdate(name=name, price=price)

      if op_type == 1:
        response = self.courses.save(data)
      elif op_type == 2:
        course_id = state_data["id"]
        response = self.courses.update_one(course_id, data)

      self.user_state.delete(user_id)

      if "error" in response:
        response = try_except(response["error"])
      else:
        response = "Hecho"
      await update.message.reply_text(response)