from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import json
import os
from .modules.config import CLIENT_PATH, DB_PATH, seed_db

seed_db()

app = FastAPI()

class CourseIn(BaseModel):
  name: str
  price: float

class CourseOut(BaseModel):
  id: int
  name: str
  price: float

def read_db():
  with open(DB_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
    return data
  
def write_db(data):
  with open(DB_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

@app.get("/api/courses", response_model=List[CourseOut])
async def get_courses():
  data = read_db()
  if not len(data.get("courses", [])) > 0:
    raise HTTPException(status_code=404, detail="Courses not found") 
  return data.get("courses", [])

@app.post("/api/courses", status_code=status.HTTP_201_CREATED)
async def add_course(course: CourseIn):
  data = read_db()
  courses = read_db().get("courses")
  if len(courses) > 0:
    last_item = courses[-1]
    id = int(last_item["id"]) + 1 
  else: id = 1
  new_course = {"id": id, "name": course.name, "price": course.price}
  try:
    courses.append(new_course)
    data["courses"] = courses
    write_db(data)
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error when save on db")
  return status.HTTP_201_CREATED

app.mount("/", StaticFiles(directory=CLIENT_PATH, html=True), name="client")