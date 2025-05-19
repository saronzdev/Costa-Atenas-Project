def format_list_courses(courses: list[dict]) -> str:
  response = ""
  lens = [len(course["name"]) for course in courses]
  sep = "+" + "----" * max(lens) + "+"
  for course in courses:
    response = f"{response}\nID: {course["id"]}\nNombre: {course["name"]}\nPrecio: {course["price"]}\n{sep}"
  return response

def format_course(course: dict) -> str:
  return f"ID: {course["id"]}\nNombre: {course["name"]}\nPrecio: {course["price"]}"
 
def set_query_update(course: dict) -> list:
  set_clause = ", ".join([f"{field} = ?" for field in course])
  values = list(course.values())
  query = f"UPDATE courses SET {set_clause} WHERE id = ?"
  return [query, values]

errors = [{404: "No encontrado", 500: "Error del servidor"}]

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
