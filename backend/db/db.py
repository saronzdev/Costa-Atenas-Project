from backend.modules import config 
import sqlite3

def get_db():
  conn = sqlite3.connect(config.DB_DIR, check_same_thread=False)
  conn.row_factory = sqlite3.Row
  try:
    yield conn
  finally:
    conn.close()


