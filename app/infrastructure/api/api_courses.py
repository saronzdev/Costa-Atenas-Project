import config
import requests
from app.application.models import CourseUpdate, CourseIn

def get_all():
  print(config.API_URL)
  try:
    response = requests.get(config.API_URL)
    response.raise_for_status()
    return response.json()
  except requests.RequestException as e:
    return {"error": str(e)}

def get_one(id: int):
  try:
    response = requests.get(f"{config.API_URL}{id}")
    response.raise_for_status()
    return response.json()
  except requests.RequestException as e:
    return {"error": str(e)}

def post(course: CourseIn):
  data = course.model_dump()
  try:
    response = requests.post(
      config.API_URL,
      json=data,
      headers={"Content-Type": "application/json"},
    )
    response.raise_for_status()
    return "Curso añadido correctamente."
  except requests.RequestException as e:
    return {"error": str(e)}

def put(id: int, course: CourseUpdate):
  url = f"{config.API_URL}{id}"
  try:
    response = requests.put(
      url,
      json=course.model_dump(exclude_none=True),
      headers={"Content-Type": "application/json"},
    )
    response.raise_for_status()
    
    return "Curso actuaizado correctamente."
  
  except requests.RequestException as e:
    return {"error": str(e)}

def delete(id: int):
  try:
    url = f"{config.API_URL}{id}"
    response = requests.delete(url)
    response.raise_for_status()
    return "Curso eliminado correctamente"
  except requests.RequestException as e:
    return {"error": str(e)}
  
