from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import json
import os
from modules.config import DB_PATH, seed_db

seed_db()

app = FastAPI()

class Course(BaseModel):
  id: int
  name: str
  price: float

def read_db():
  with open(DB_PATH, "r") as f:
    return json.load(f)
  
def write_db(data):
  with open(DB_PATH, "w") as f:
    json.dump(data, f, indent=4)

@app.get("/api/courses", response_model=List[Course])
async def get_courses():
  data = read_db()
  return data.get("courses", [])

@app.post("/api/courses", )
async def add_course(course: Course):
  data = read_db()
  data["courses"].append(course)
  write_db(data)
  return {"message: Curso Guardado"}

app.mount("/", StaticFiles(directory="../client", html=True), name="client")