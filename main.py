from app.infrastructure.telegram_bot import start_telegram_bot
from app.infrastructure.fastapi_server import start_fastapi_server

if __name__ == "__main__":
  import threading
  threading.Thread(target=start_fastapi_server, daemon=True).start()
  start_telegram_bot()
  