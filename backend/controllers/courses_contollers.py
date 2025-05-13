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
  if not new: return 2
  new = new.model_dump(exclude_unset=True)
  set_clause = ", ".join([f"{field} = ?" for field in new])
  values = list(new.values())
  values.append(id)
  query = f"UPDATE courses SET {set_clause} WHERE id = ?"

  cursor = db.cursor()
  cursor.execute(query, values)
  db.commit()
  
  if cursor.rowcount == 0: return 1

  return 0