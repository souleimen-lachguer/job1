def trier_liste(l):
    # On continue tant que des échanges sont faits
    echanges = True
    while echanges:
        echanges = False
        # Parcourir la liste
        for i in range(0, len(l) - 1):
            # Comparer l'élément actuel avec le suivant
            if l[i] > l[i + 1]:
                # Si l'élément actuel est plus grand, on les échange
                l[i], l[i + 1] = l[i + 1], l[i]
                echanges = True

# Exemple d'utilisation
L = [42, 7, 11, 39, 2]
trier_liste(L)
print("Liste triée :", L)