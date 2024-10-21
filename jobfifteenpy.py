# Fonction pour arrondir un nombre sans utiliser round()
def arrondir_nombre(nombre):
    # Séparer la partie entière et la partie décimale
    entier = int(nombre)  # Partie entière
    decimal = nombre - entier  # Partie décimale

    # Arrondir en fonction de la partie décimale
    if decimal < 0.5:
        return entier  # Arrondi vers le bas
    else:
        return entier + 1  # Arrondi vers le haut

# Fonction pour trier la liste dans l'ordre croissant
def trier_liste(liste):
    # Utilisation du tri à bulles (bubble sort)
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                # Échanger les éléments s'ils ne sont pas dans l'ordre
                liste[j], liste[j+1] = liste[j+1], liste[j]

# Liste donnée
L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir chaque élément de la liste
L_arrondie = []
for nombre in L:
    L_arrondie.append(arrondir_nombre(nombre))

# Trier la liste arrondie
trier_liste(L_arrondie)

# Affichage de la liste finale
print("Liste arrondie et triée :", L_arrondie)