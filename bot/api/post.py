from modules import config
import requests

async def post(data: list):
  name = data[0]
  price = data[1]
  
  new_course = {"name": name, "price": price}
 
  response = requests.post(
    config.API_URL,
    json=new_course,
    headers={"Content-Type": "application/json"},
  )
  
  if response.status_code != 201: return "Ha ocurrido un error inesperado."
  return "Curso añadido correctamente."