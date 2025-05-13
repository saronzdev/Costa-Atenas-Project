from modules import config
import requests

async def put(id: int, data: list):
  name = data[0]
  price = data[1]

  new_course = {"name": name, "price": price}
  
  if name == "-": del new_course["name"]
  if price == "-": del new_course["price"]

  print(new_course)

  url = f"{config.API_URL}{id}"
  
  response = requests.put(
    url,
    json=new_course,
    headers={"Content-Type": "application/json"},
  )
  
  if response.status_code != 200: return "Ha ocurrido un error inesperado."
  return "Curso actuaizado correctamente."