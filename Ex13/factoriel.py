def factoriel(n:int) -> int:
  if n == 0:
    return 1
  else:
    result = 1
    for i in range(result, n + 1):
      result *= i
    return result
  # Récursif
  # else:
  #   return n * factoriel(n-1)

print(factoriel(7))