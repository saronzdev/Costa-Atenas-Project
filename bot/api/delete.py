from modules import config
import requests

async def delete(id: int):
  url = f"{config.API_URL}{id}"
  response = requests.delete(url)
  if response.status_code == 404: return "Curso no encontrado" 
  return "Curso eliminado correctamente"