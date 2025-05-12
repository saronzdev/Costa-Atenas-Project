import json
from modules import config 

def read_db():
  with open(config.DB_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
    return data
  
def write_db(data):
  with open(config.DB_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)