from src.infrastructure.telegram_bot import start_telegram_bot
from src.infrastructure.fastapi_server import start_fastapi_server

if __name__ == "__main__":
    import threading

    threading.Thread(target=start_fastapi_server, daemon=True).start()
    print(f"\n🌐 Servidor web iniciado en http://127.0.0.1:3000")
    start_telegram_bot()
