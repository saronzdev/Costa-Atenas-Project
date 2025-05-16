from modules import config
import requests

async def get_all():
  response = requests.get(config.API_URL)
  if response.status_code == 404: return "No hay cursos disponibles"
  courses = response.json()
  result = []
  for course in courses:
    result.append(f"ID: {course["id"]}\nNombre: {course["name"]}\nPrecio: {course["price"]}") 
  
  return "\n\n".join(result)

async def get_one(id: int):
  response = requests.get(f"{config.API_URL}{id}")
  if response.status_code == 404: return "Curso no encontrado"
  course = response.json()
  
  return f"ID: {course["id"]}\nNombre: {course["name"]}\nPrecio: {course["price"]}"