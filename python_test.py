import tkinter as tk
import random
import json

#parametres du jeu
taille_case = 100
taille_grille = 4
marge = 4
couleur_fond = "beige"
couleur_case_vide = "gray"
couleurs_bloc = {
    2: "#EEE4DA", 4: "#EDE0C8", 8: "#F2B179", 16: "#F59563",
    32: "#F67C5F", 64: "#F65E3B", 128: "#EDCF72", 256: "#EDCC61",
    512: "#EDC850", 1024: "#EDC53F", 2048: "#EDC22E"
}
couleurs_texte = {2: "#776E65", 4: "#776E65", 8: "#F9F6F2"}

class MenuPrincipal:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("2048 - Menu")
        self.fenetre.geometry("300x200")
        self.fenetre.configure(bg="beige")

        titre = tk.Label(self.fenetre, text=2048, font=("Arial", 32, "bold"), bg="beige")
        titre.pack(pady=20)

        bouton_jouer = tk.Button(self.fenetre, text="Jouer", font=("Arial", 16), command=self.lancer_jeu, bg="#8BC34A", fg="white")
        bouton_jouer.pack(pady=10)

        bouton_quitter = tk.Button(self.fenetre, text="Quitter", font=("Arial", 12), command=self.fenetre.destroy, bg="red", fg="white")
        bouton_quitter.pack(pady=5)

        self.fenetre.mainloop()

    def lancer_jeu(self):
        self.fenetre.destroy()
        Game2048()


class Game2048:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("2048")
        self.fenetre.resizable(False, False)
        self.grille = [[0] * taille_grille for _ in range(taille_grille)]
        self.creer_interface()
        self.charger_sauvegarde()
        self.mettre_a_jour_interface()
        self.fenetre.bind("<Key>", self.touches)
        self.fenetre.mainloop()

    

    def touches(self, event):
        if event.keysym in ("Up", "Down", "Left", "Right"):
            deplace = self.deplacer(event.keysym)
            if deplace:
                self.ajouter_bloc()
                self.mettre_a_jour_interface()
                if self.est_fin_de_jeu():
                    self.afficher_fin_jeu()

    

if __name__ == "__main__":
    MenuPrincipal()
