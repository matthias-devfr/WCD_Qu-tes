import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Horloge")

# Configuration de l'étiquette pour afficher l'heure
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')

# Placement de l'étiquette dans la fenêtre
label.pack(anchor='center')

# Exécution de la fonction time pour mettre à jour l'heure
time()

# Boucle principale de la fenêtre
root.mainloop()
