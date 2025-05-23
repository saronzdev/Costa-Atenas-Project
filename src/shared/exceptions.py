def try_except(code: int):
  if code == 404:
    return ValueError("No encontrado")
  if code == 400:
    return ValueError("Petición incorrecta")
  if code == 500:
    return ValueError("Error no controlado")