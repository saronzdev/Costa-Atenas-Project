import sqlite3
from backend.models import courses_models

def get_courses(db: sqlite3.Connection):
  cursor = db.cursor()
  cursor.execute("SELECT * FROM courses")
  courses = cursor.fetchall() 
  if len(courses) > 0: return [dict(row) for row in courses] 
  return 1

async def add_course(course: courses_models.CourseIn, db: sqlite3.Connection):
  cursor = db.cursor()
  cursor.execute("INSERT INTO courses (name, price) VALUES (?, ?)", (course.name, course.price))
  db.commit()
  return 0

async def del_course(id: int, db: sqlite3.Connection):
  cursor = db.cursor()
  cursor.execute("DELETE FROM courses WHERE id = ?", (id,))
  db.commit()
  return 0

async def update_course(new: courses_models.CourseIn, id: int, db: sqlite3.Connection):
  cursor = db.cursor()
  cursor.execute("UPDATE courses SET name = ?, price = ? WHERE id = ?", (new.name, new.price, id))
  db.commit()
  return 0