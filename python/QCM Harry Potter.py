# Définition de la classe Question pour représenter une question du quiz
class Question:
    def __init__(self, text, options, correct_option):
        # Initialisation des attributs de la question
        self.text = text
        self.options = options
        self.correct_option = correct_option

# Fonction pour exécuter le quiz avec la liste de questions en entrée
def run_quiz(questions):
    score = 0  # Initialisation du score
    for i, question in enumerate(questions, 1):
        # Affichage de la question et de ses options
        print(f"\nQuestion {i}: {question.text}")
        for j, option in enumerate(question.options, 1):
            print(f"{j}. {option}")

        # Saisie de la réponse de l'utilisateur
        user_answer = int(input("Choisissez la bonne réponse : "))
        
        # Vérification de la réponse et mise à jour du score
        if user_answer == question.correct_option:
            print("Bonne réponse !")
            score += 1
        else:
            print(f"Mauvaise réponse. La bonne réponse était l'option {question.correct_option}.")

    # Affichage du score final
    print(f"\nVotre score final est : {score}/{len(questions)}")
    input("Appuyez sur une touche pour fermer le programme.")

# Liste d'exemples de questions

questions = [
    Question("Quelle est la maison à laquelle Harry Potter appartient à Poudlard ?", ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"], 1),
    Question("Quel est le nom du professeur de potions à Poudlard dans la plupart des livres de la série ?", ["Remus Lupin", "Gilderoy Lockhart", "Severus Rogue", "Alastor Maugrey"], 3),
    Question("Quel animal est l'Animagus de Sirius Black ?", ["Chat", "Loup", "Rat", "Chien"], 4),
    Question("Quel est le sortilège utilisé pour invoquer un Patronus ?", ["Expelliarmus", "Expecto Patronum", "Stupefy", "Accio"], 2),
    Question("Qui est le directeur de Poudlard dans le premier livre de la série ?", ["Albus Dumbledore", "Minerva McGonagall", "Severus Rogue", "Remus Lupin"], 1),
    Question("Quel est le nom du balai volant que Harry reçoit comme cadeau dans 'Harry Potter à l'école des sorciers' ?", ["Nimbus 2000", "Firebolt", "Cleansweep Seven", "Comet 260"], 1),
    Question("Quel est le nom du gobelin de la banque Gringotts qui accompagne Harry et Hagrid dans le premier livre ?", ["Griphook", "Ragnok", "Bogrod", "Tragnok"], 1),
    Question("Quel est le nom du frère de Ron Weasley ?", ["Fred", "Neville", "Dudley", "Voldemort"], 1),
    Question("Dans quel livre Harry Potter découvre-t-il qu'il est un Fourchelangue, capable de parler aux serpents ?", ["Harry Potter à l'école des sorciers", "Harry Potter et la Chambre des secrets", "Harry Potter et le Prisonnier d'Azkaban"], 2),
    Question("Quel est le nom de la baguette magique de Harry Potter ?", ["Baguette de Saule", "Baguette de Houx", "Baguette de Sorbier", "Baguette de Noyer"], 2),
    Question("Quel est le nom du gardien des clés et des lieux à Poudlard ?", ["Dobby", "Kreattur", "Norbert Dragonneau", "Rubeus Hagrid"], 4),
    Question("Quelle est la matière enseignée par Gilderoy Lockhart à Poudlard ?", ["Défense contre les Forces du Mal", "Sortilèges", "Botanique", "Soins aux créatures magiques"], 1),
    Question("Quel est le nom de la prison des sorciers ?", ["Azkaban", "Nurmengard", "Gringotts", "Le Terrier"], 1),
    Question("Quel est le nom de la boutique des jumeaux Weasley à Pré-au-Lard ?", ["Ollivander", "Farces pour sorciers facétieux", "Zonko", "Le Chaudron Baveur"], 2),
    Question("Qui est le professeur de Divination à Poudlard ?", ["Sybille Trelawney", "Filius Flitwick", "Pomona Chourave", "Firenze"], 1),
    Question("Quel est le nom de l'elfe de maison qui appartient à la famille Malefoy ?", ["Kreattur", "Winky", "Dobby", "Hokey"], 3),
    Question("Dans quel livre Harry Potter découvre-t-il le nom de Tom Jedusor ?", ["Harry Potter à l'école des sorciers", "Harry Potter et la Coupe de Feu", "Harry Potter et le Prisonnier d'Azkaban", "Harry Potter et la Chambre des secrets"], 4),
    Question("Quel est le nom du serpent de Voldemort ?", ["Niffler", "Nagano", "Narsil", "Nagini"], 4),
    Question("Comment s'appelle le frère de Dumbledore ?", ["Abelforth ", "Alastor", "fletwey", "Aeron"], 1),
    Question("Quelle est la nationalité de Viktor Krum, le joueur de Quidditch de l'équipe des Harpies de Holyhead ?", ["Écossaise", "Irlandaise", "Bulgare", "Française"], 3),
]


# Exécution du quiz avec les questions définies
run_quiz(questions)
