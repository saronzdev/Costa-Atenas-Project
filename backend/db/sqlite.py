from backend.modules import config 
import sqlite3

conn = sqlite3.connect(config.SQLITE_DB_PATH)
cursor = conn.cursor()

def seed_db_sqlite():
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      price REAL NOT NULL            
    )               
  ''')
conn.commit()

def read_db():
  cursor.execute("SELECT * FROM courses")
  courses = cursor.fetchall()
  return courses