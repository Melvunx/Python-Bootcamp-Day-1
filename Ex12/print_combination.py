def print_combination():
    combinations = []
    for i in range(10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                # Concatène les chiffres et les ajoute au format souhaité
                combinations.append(f"{i}{j}{k}")
    
    # Affiche les combinaisons séparées par des virgules
    print(", ".join(combinations))

# Appel de la fonction
print_combination()
