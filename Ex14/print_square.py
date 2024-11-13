def print_lenght(n: int) -> None:
  if n < 2:
    print("longueur non suffisante")
    return
  print("*" + "-" * (n - 2) + "*")

def print_width(n: int) -> None:
  if n < 2:
    print("largeur non suffisante")
    return
  for _ in range(n - 2):
    print("|" + " " * (n - 2) + "|")

def print_square(n: int) -> None:
  print_lenght(n)
  print_width(n)
  print_lenght(n)

# Exemple d'utilisation
print_square(6)
