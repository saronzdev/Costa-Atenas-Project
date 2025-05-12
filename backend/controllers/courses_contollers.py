from backend.db import json, sqlite
from backend.models import courses_models

async def get_courses():
  data = sqlite.read_db() # json.read_db()
  # if not len(data.get("courses", [])) > 0: return 1 
  if not len(data) > 0: return 1
  print(data) 
  return data

async def add_course(course: courses_models.CourseIn):
  data = json.read_db()
  courses = json.read_db().get("courses")
  
  id = int(courses[-1]["id"]) + 1  if len(courses) > 0 else 1
  new_course = {"id": id, "name": course.name, "price": course.price}
  
  courses.append(new_course)
  data["courses"] = courses
  json.write_db(data)
  return 0

async def del_course(id: int):
  data = json.read_db()
  courses = data.get("courses")
  for i, course in enumerate(courses):
    if id == course["id"]:
      courses.pop(i)
      data["courses"] = courses
      json.write_db(data)
      return 0
  
  return 1

async def update_course(new: courses_models.CourseIn, id: int):
  data = json.read_db()
  courses = data.get("courses")
  
  for i, course in enumerate(courses):
    if id == course["id"]:
      courses[i].update(new)
      data["courses"] = courses
      json.write_db(data)
      return 0
  
  return 1