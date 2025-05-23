def format_list_courses(courses: list[dict]) -> str:
  response = ""
  lens = [len(course["name"]) for course in courses]
  sep = "+" + "----" * max(lens) + "+"
  for course in courses:
    response = f"{response}\nID: {course["id"]}\nNombre: {course["name"]}\nPrecio: {course["price"]}\n{sep}"
  return response

def format_course(course: dict) -> str:
  return f"ID: {course["id"]}\nNombre: {course["name"]}\nPrecio: {course["price"]}"
