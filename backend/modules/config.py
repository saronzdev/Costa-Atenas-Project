from pathlib import Path
import os

DB_PATH = Path(__file__).parent.parent / "db.json"
CLIENT_PATH = Path(__file__).parent.parent.parent / "client"

def seed_db():
  if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
      f.write("""{
  "courses": []
}""") 