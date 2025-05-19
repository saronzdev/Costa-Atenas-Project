from app.infrastructure.database.db import get_connection
from app.application.models import CourseIn
from app.domain.services import set_query_update

def get_all():
  with get_connection() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    if cursor.rowcount == 0: return {"error": 404}
    return cursor.fetchall()

def get_one(id: int):
  with get_connection() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses WHERE id = ?", (id,))
    course = cursor.fetchone()
    if not course: return {"error": 404}
    return course
  
def create(course: CourseIn):
  with get_connection() as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (name, price) VALUES (?, ?)", (course.name, course.price))
    conn.commit()
    return {"ok": True}

def update(id: int, course: dict):
  query = set_query_update(course)
  query[1].append(id)
  with get_connection() as conn:
    cursor = conn.cursor()
    cursor.execute(query[0], query[1])
    if cursor.rowcount == 0: return {"error": 404}
    conn.commit()
    return {"ok": True}

def delete(id: int):
  with get_connection() as conn:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE id = ?", (id,))
    if cursor.rowcount == 0: return {"error": 404}
    conn.commit()
    return {"ok": True}