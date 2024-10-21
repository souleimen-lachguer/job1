def my_long_word(n, phrase):
    # Variable pour stocker le résultat
    result = []
    # Variable pour stocker temporairement un mot
    mot = ""
    
    # Parcourir chaque caractère de la phrase
    for char in phrase:
        if char != " " and char != "," and char != ".":  # Si le caractère n'est pas un espace ou une ponctuation
            mot += char  # Construire le mot caractère par caractère
        else:
            if mot:  # Si un mot est complété
                # Compter le nombre de caractères dans le mot
                count = 0
                for _ in mot:
                    count += 1
                # Si le mot est plus long que n, on l'ajoute au résultat
                if count > n:
                    result.append(mot)
                mot = ""  # Réinitialiser le mot après traitement
    
    # Traiter le dernier mot s'il existe (quand il n'y a pas de ponctuation finale)
    if mot:
        count = 0
        for _ in mot:
            count += 1
        if count > n:
            result.append(mot)

    # Retourner les mots sous forme de chaîne de caractères
    return " ".join(result)

# Exemple d'utilisation
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
output = my_long_word(3, phrase)

# Affichage du résultat
print(output)