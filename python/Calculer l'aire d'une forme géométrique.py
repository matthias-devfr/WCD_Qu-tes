import math

# Fonction pour calculer l'aire d'un triangle
def calculer_aire_triangle(base, hauteur):
    return 0.5 * base * hauteur

# Fonction pour calculer l'aire d'un carré
def calculer_aire_carre(cote):
    return cote * cote

# Fonction pour calculer l'aire d'un rectangle
def calculer_aire_rectangle(longueur, largeur):
    return longueur * largeur

# Fonction pour calculer l'aire d'un cercle
def calculer_aire_cercle(rayon):
    return math.pi * rayon ** 2

# Fonction principale du programme
def main():
    while True:
        # Affichage du menu pour choisir la figure géométrique
        print("Choisissez la figure géométrique pour calculer l'aire:")
        print("1. Triangle")
        print("2. Carré")
        print("3. Rectangle")
        print("4. Cercle")

        # Saisie du choix de l'utilisateur
        choix = input("Entrez le numéro de la figure choisie (1/2/3/4): ")

        # Branchement sur le choix de l'utilisateur
        if choix == '1':
            base = float(input("Entrez la base du triangle : "))
            hauteur = float(input("Entrez la hauteur du triangle : "))
            aire = calculer_aire_triangle(base, hauteur)
            print(f"L'aire du triangle est : {aire}")
        elif choix == '2':
            cote = float(input("Entrez la longueur du côté du carré : "))
            aire = calculer_aire_carre(cote)
            print(f"L'aire du carré est : {aire}")
        elif choix == '3':
            longueur = float(input("Entrez la longueur du rectangle : "))
            largeur = float(input("Entrez la largeur du rectangle : "))
            aire = calculer_aire_rectangle(longueur, largeur)
            print(f"L'aire du rectangle est : {aire}")
        elif choix == '4':
            rayon = float(input("Entrez le rayon du cercle : "))
            aire = calculer_aire_cercle(rayon)
            print(f"L'aire du cercle est : {aire}")
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")

        # Demande à l'utilisateur s'il souhaite continuer à calculer
        continuer = input("Voulez-vous continuer à calculer ? (o/n): ")
        if continuer.lower() != 'o':
            print("Programme terminé.")
            break

# Point d'entrée du programme
if __name__ == "__main__":
    main()