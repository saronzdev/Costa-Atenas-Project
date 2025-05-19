# Repositorio oficial del bot, backend y fronted del proyecto Costa Atenas

## Enlaces:
- 🤖 [Bot de Telegram](https://t.me/test_509_bot)
- 🌐 Web (en desarrollo)

---

## 🛠️ Instrucciones para ejecutar el backend, frontend y el bot

### En Linux:
1. Abre una terminal en la carpeta raíz del proyecto.
2. Ejecuta los siguientes comandos:

```bash
./run_bot.sh        # Ejecuta el bot
./run_server.sh     # Ejecuta el servidor + frontend
````

> **Nota**: También puedes ejecutar los archivos directamente desde el explorador (asegúrate de que tengan permisos de ejecución).

### En Windows:

1. Abre CMD o PowerShell en la carpeta raíz del proyecto.
2. Ejecuta los siguientes comandos:

```powershell
python -m app.infrastructure.telegram_bot
uvicorn app.infrastructure.fastapi_server:app --reload --port 3000
```
