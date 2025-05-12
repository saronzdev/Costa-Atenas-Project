from ..db.operations import read_db, write_db
from fastapi import HTTPException, status
from models import models

async def get_courses():
  data = read_db()
  if not len(data.get("courses", [])) > 0:
    return 1 
  return data.get("courses", [])

async def add_course(course: models.CourseIn):
  data = read_db()
  courses = read_db().get("courses")
  if len(courses) > 0:
    last_item = courses[-1]
    id = int(last_item["id"]) + 1
  else: id = 1
  new_course = {"id": id, "name": course.name, "price": course.price}
  courses.append(new_course)
  data["courses"] = courses
  write_db(data)
  return 0

async def del_course(id: int):
  data = read_db()
  courses = data.get("courses")
  for i, course in enumerate(courses):
    if id == course["id"]:
      courses.pop(i)
      data["courses"] = courses
      write_db(data)
      return 0
  
  return 1

async def update_course(new: models.CourseIn, id: int):
  data = read_db()
  courses = data.get("courses")
  
  for i, course in enumerate(courses):
    if id == course["id"]:
      courses[i].update(new)
      data["courses"] = courses
      write_db(data)
      return 0
  
  return 1