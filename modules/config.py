import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DB_PATH = Path(__file__).parent.parent / "db.json"
BOT_TOKEN = os.getenv("BOT_TOKEN") 
API_URL = "localhost:3000/data"

def seed():
  if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
      f.write("[]") 