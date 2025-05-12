import json
import os
from backend.modules import config 

def seed_db():
  if not os.path.exists(config.DB_PATH):
    with open(config.DB_PATH, "w") as f:
      f.write("""{
  "courses": []
}""") 

def read_db():
  with open(config.DB_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
    return data
  
def write_db(data):
  with open(config.DB_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)