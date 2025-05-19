import config 
import sqlite3

def get_connection() -> sqlite3.Connection:
  conn = sqlite3.connect(config.DB_DIR, check_same_thread=False)
  conn.row_factory = sqlite3.Row
  return conn

def init_db():
  with get_connection() as conn:
    cursor = conn.cursor()
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL            
      )               
    ''')
    conn.commit()