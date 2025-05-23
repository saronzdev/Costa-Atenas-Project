from src.shared import schemas
from src.shared.utils import set_query_update
import sqlite3

class CoursesRepository():
  def __init__(self, db_path: str):
    self.conn = sqlite3.connect(db_path, check_same_thread=False)
    self.conn.row_factory = sqlite3.Row
    self._create_table()

  def _create_table(self):
    cursor = self.conn.cursor()
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL            
      )               
    ''')
    self.conn.commit()

  def create_new_course(self, course: schemas.CourseIn):
    coursor = self.conn.cursor()
    coursor.execute("INSERT INTO courses (name, price) VALUES (?, ?)", [course.name, course.price])
    self.conn.commit()
    
    return {"ok": True}

  def find_courses(self) -> list[schemas.CourseOut]:
    cursor = self.conn.cursor()
    cursor.execute("SELECT * FROM courses")
    
    if cursor.rowcount == 0: return {"error": 404}
    return cursor.fetchall()

  def find_course_by_id(self, id: int):
    cursor = self.conn.cursor()
    cursor.execute("SELECT * FROM courses WHERE id = ?", [id])
    course = cursor.fetchone()
    
    if not course: return {"error": 404}
    return course 

  def update_course_by_id(self, id: int, course: dict):
    fields, params = set_query_update(course)
    params.append(id)

    cursor = self.conn.cursor()
    cursor.execute(f"UPDATE courses SET {", ".join(fields)} WHERE id = ?", params)
    
    if cursor.rowcount == 0: return {"error": 404}
    
    self.conn.commit()
    return {"ok": True}

  def delete_course_by_id(self, id: int):
    cursor = self.conn.cursor()
    cursor.execute("DELETE FROM courses WHERE id = ?", [id])
    
    if cursor.rowcount == 0: return {"error": 404}
    self.conn.commit()
    
    return {"ok": True}  
  

