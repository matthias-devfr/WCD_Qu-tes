# Fonction pour afficher le message de bienvenue
def print_welcome_message():
    print("Bienvenue sur la mini-calculatrice !")

# Fonction pour saisir deux nombres en boucle jusqu'à ce que des valeurs valides soient entrées
def input_two_numbers():
    while True:
        try:
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le deuxième nombre : "))
            return num1, num2
        except ValueError:
            print("Veuillez entrer des nombres valides.")

# Fonction pour afficher le menu et obtenir le choix de l'utilisateur
def print_menu_and_get_choice():
    print("=== MENU ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        user_choice = input("Entrez votre choix (1-4) : ")
        if user_choice in ["1", "2", "3", "4"]:
            return user_choice
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

# Fonction pour exécuter le calcul en fonction du choix de l'utilisateur
def run_calculation(user_choice, num1, num2):
    if user_choice == '1':
        result = num1 + num2
    elif user_choice == '2':
        result = num1 - num2
    elif user_choice == '3':
        result = num1 * num2
    elif user_choice == '4':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Erreur : division par zéro")
            return None
    else:
        print("Choix invalide.")
        return None

    return result

# Point d'entrée du programme
if __name__ == '__main__':
    # Afficher le message de bienvenue
    print_welcome_message()

    # Obtenir le choix de l'utilisateur et saisir les deux nombres
    user_choice = print_menu_and_get_choice()
    num1, num2 = input_two_numbers()

    # Exécuter le calcul en fonction du choix de l'utilisateur
    result = run_calculation(user_choice, num1, num2)

    # Afficher le résultat si le calcul a réussi
    if result is not None:
        print("Résultat : ", result)
