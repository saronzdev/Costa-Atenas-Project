from fastapi import HTTPException
import sqlite3
from backend.models import courses_models

def get_courses(db: sqlite3.Connection):
  cursor = db.cursor()
  cursor.execute("SELECT * FROM courses")
  courses = cursor.fetchall() 
  if cursor.rowcount == 0: raise HTTPException(status_code=404) 
  
  return [dict(row) for row in courses] 

def get_course(id: int, db: sqlite3.Connection):
  cursor = db.cursor()
  cursor.execute("SELECT * FROM courses WHERE id = ?", (id,))
  course = cursor.fetchone()
  if not course: raise HTTPException(status_code=404)
  return dict(course)

async def add_course(course: courses_models.CourseIn, db: sqlite3.Connection):
  cursor = db.cursor()
  
  cursor.execute("INSERT INTO courses (name, price) VALUES (?, ?)", (course.name, course.price))
  
  db.commit()
  return

async def del_course(id: int, db: sqlite3.Connection):
  cursor = db.cursor()
  
  cursor.execute("DELETE FROM courses WHERE id = ?", (id,))
  if cursor.rowcount == 0:
    raise HTTPException(status_code=404)
  
  db.commit()
  return

async def update_course(new: courses_models.CourseIn, id: int, db: sqlite3.Connection):
  if not new: return 2
  new = new.model_dump(exclude_unset=True)
  set_clause = ", ".join([f"{field} = ?" for field in new])
  values = list(new.values())
  values.append(id)
  query = f"UPDATE courses SET {set_clause} WHERE id = ?"

  cursor = db.cursor()
  cursor.execute(query, values)
  if cursor.rowcount == 0: raise HTTPException(status_code=404)
  
  db.commit()
  return