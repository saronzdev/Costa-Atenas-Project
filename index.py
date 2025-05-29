def fibo(pos: int):
  base = [0, 1]
  while len(base) != pos:
    new_value = base[-1] + base[-2]
    base.append(new_value)
  
  return base

print(fibo(8))