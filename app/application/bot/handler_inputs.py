from telegram import Update
from telegram.ext import ContextTypes
import config
from app.infrastructure.api import api_courses
from app.application.models import CourseIn, CourseUpdate

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    data = CourseUpdate(name=name, price=price)

    if type == 1:
      response = api_courses.post(data)
    elif type == 2:
      id = config.user_states[user_id]["id"]
      response = api_courses.put(id, data)

    del config.user_states[user_id]

    if "error" in response: response = response["error"].split(":")[0]  
    await update.message.reply_text(response)
