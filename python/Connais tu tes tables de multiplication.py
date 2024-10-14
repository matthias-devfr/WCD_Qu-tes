# Importation du module random pour générer des nombres aléatoires
import random

# Fonction pour générer une question aléatoire de multiplication
def generer_question():
    # Génération de deux nombres aléatoires entre 2 et 9 inclus
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    # Calcul de la réponse correcte
    reponse_correcte = a * b
    return a, b, reponse_correcte

# Fonction pour afficher le score actuel
def afficher_score(score):
    print(f"Score actuel: {score}\n")

# Fonction principale du programme
def main():
    # Initialisation du score à 0 et du nombre de questions à 20
    score = 0
    nombre_questions = 20

    # Boucle pour poser le nombre prédéfini de questions
    for _ in range(nombre_questions):
        # Appel de la fonction pour générer une question
        a, b, reponse_correcte = generer_question()
        # Création de la question sous forme de chaîne de caractères
        question = f"Combien font {a} * {b} ? "

        # Tentative de lecture de la réponse de l'utilisateur
        try:
            reponse_utilisateur = int(input(question))
        except ValueError:
            # Gestion de l'exception si l'utilisateur entre autre chose qu'un nombre entier
            print("Tu dois entrer un nombre entier.")
            continue

        # Vérification de la réponse de l'utilisateur et mise à jour du score
        if reponse_utilisateur == reponse_correcte:
            print("Super ! Bien joué !")
            score += 1
        else:
            print(f"La réponse est Incorrecte. La bonne réponse était {reponse_correcte}.")

    # Affichage du score final
    print(f"\nTon score final est de {score}/{nombre_questions}.")

    # Demande à l'utilisateur s'il veut refaire une partie
    continuer_partie = input("Veux-tu refaire une partie ? (O ou N) ")
    if continuer_partie.lower() == 'o' or continuer_partie.lower() == 'O':
        # Si la réponse est 'O' ou 'o', relancer le jeu
        main()
    else:
        # Sinon, afficher que le programme est terminé
        print("Programme terminé.")

# Point d'entrée du programme
if __name__ == "__main__":
    # Appel de la fonction principale si le script est exécuté en tant que programme principal
    main()
