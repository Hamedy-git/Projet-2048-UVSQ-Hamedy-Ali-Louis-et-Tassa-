import tkinter as tk
import random
import json

case_taille = 100
canvas_grid = 4
marge = 4

class MenuPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("2048 - Menu")
        self.root.geometry("300x200")
        self.root.configure(bg="beige")

        titre = tk.Label(self.root, text="2048", font=("Arial", 32, "bold"), bg="beige")
        titre.pack(pady=20)

        self.root.mainloop()

    def lancer_jeu(self):
        self.root.destroy() # Ferme le jeu
        Game2048() # Lance le jeu 


class Game2048:
    def __init__(self):
        self.racine = tk.Tk()
        self.racine.title("2048")
        self.racine.resizable(False, False)
        self.grid = [[0] * canvas_grid for _ in range(canvas_grid)]
        self.init_ui() # initialise l'interface
        self.charger_progression() # Charge une sauvegarde 
        self.interface()  # dessine la grille
        self.racine.bind("<Key>", self.touches) # Lie les touches 
        self.racine.mainloop()

    
    def cree_block(self): # Ajoute un nouveau block (2 ou 4) à un emplacement vide
        case_vide = [(i, j) for i in range(canvas_grid) for j in range(canvas_grid) if self.grid[i][j] == 0]
        if case_vide:
            i, j = random.choice(case_vide)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4




    
if __name__ == "__main__":
    MenuPrincipal()