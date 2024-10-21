def supprimer_doublons(liste):
    nouvelle_liste = []
    for element in liste:
        if element not in nouvelle_liste:
            nouvelle_liste.append(element)
    return nouvelle_liste

# Liste d'origine avec doublons
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Appel de la fonction pour supprimer les doublons
L_sans_doublons = supprimer_doublons(L)

# Affichage de la liste sans doublons
print("Liste sans doublons :", L_sans_doublons)