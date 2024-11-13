def fibonacci(n: int):
    # Cas où n est inférieur ou égal à 0 : retourne une liste vide
    if n <= 0:
        return []
    # Cas où n est égal à 1 : retourne une liste contenant seulement le premier élément de la suite
    elif n == 1:
        return [0]
    
    # Initialisation de la liste avec les deux premiers éléments de la suite de Fibonacci
    fib_sequence = [0, 1]

    # Génère les éléments de la suite jusqu'à atteindre n éléments
    for i in range(2, n):
      next_value = fib_sequence[-1] + fib_sequence[-2]
      fib_sequence.append(next_value)

    return fib_sequence

# Exemple d'utilisation
print(fibonacci(10))
