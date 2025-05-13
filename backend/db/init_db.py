import sqlite3
from backend.modules import config

def init():
  conn = sqlite3.connect(config.SQLITE_DB_PATH)
  cursor = conn.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      price REAL NOT NULL            
    )               
  ''')
  conn.commit()
  conn.close()