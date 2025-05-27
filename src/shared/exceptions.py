def try_except(code: int):
  if code == 404:
    return "No encontrado"
  if code == 400:
    return "Petición incorrecta"
  if code == 500:
    return "Error no controlado"