from app.application.models import CourseUpdate
from telegram import BotCommand

def format_list_courses(courses: list[dict]) -> str:
  response = ""
  for course in courses:
    response = f"{response}\n ID: {course["id"]}\nNombre: {course["name"]}\nPrecio: {course["price"]}"
  return response
 
def set_query_update(course: dict) -> list:
  set_clause = ", ".join([f"{field} = ?" for field in course])
  values = list(course.values())
  query = f"UPDATE courses SET {set_clause} WHERE id = ?"
  return [query, values]

errors = [{404: "No encontrado", 500: "Error del servidor"}]

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

def get_commands_desc() -> list:
  DESCRIPTIONS = [
    "Usa /start para inicar (o reiniciar) el bot",
    "Usa /help para ver más información de los commandos",
    "Usa /new_course para añadir nuevo un curso",
    "Usa /get_courses para mostar una lista de los cursos disponibles (permite búsqueda por ID)",
    "Usa /delete_course <ID> para borrar el curso con dicho ID",
    "Usa /update_course <ID> para actualizar el curso con dicho ID"
  ]
  return DESCRIPTIONS
