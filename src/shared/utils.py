from telegram import BotCommand 

def set_query_update(course: dict) -> list:
  fields = []
  params = []
  
  for key in course:
    fields.append(f"{key} = ?")

  for value in course.values():
    params.append(value)

  return fields, params

def get_commands() -> list:
  DESCRIPTIONS = [
    "Usa /start para inicar (o reiniciar) el bot",
    "Usa /help para ver más información de los commandos",
    "Usa /new_course para añadir nuevo un curso",
    "Usa /get_courses para mostar una lista de los cursos disponibles (permite búsqueda por ID)",
    "Usa /delete_course <ID> para borrar el curso con dicho ID",
    "Usa /update_course <ID> para actualizar el curso con dicho ID"
  ]
  return DESCRIPTIONS

def create_bot_commands():
  COMMANDS = [
    BotCommand("start", "Iniciar el bot"),
    BotCommand("help", "Mostrar los comandos disponibles"),
    BotCommand("new", "Añadir nuevo curso"),
    BotCommand("get", "<ID opcional> obtener cursos disponibles"),
    BotCommand("delete", "Borrar un curso"),
    BotCommand("update", "Actualizar un curso")
  ]
  return COMMANDS