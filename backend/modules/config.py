import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DB_DIR = os.path.join(BASE_DIR, "backend", "database.db")
STATIC_DIR = os.path.join(BASE_DIR, "client", "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "client", "templates")