class Duplicant:
    def __init__(self, nom, classe, attaque, defense, vie, soin, stress):
        self.nom = nom
        self.classe = classe
        self.attaque = attaque
        self.defense = defense
        self.vie = vie
        self.soin = soin
        self.stress = stress

    def afficher_infos(self):
        print(f"Nom: {self.nom}, Classe: {self.classe}")
        print(f"  ATT: {self.attaque}, DEF: {self.defense}, PV: {self.vie}, SOI: {self.soin}, STR: {self.stress}")

def creer_duplicants():
    duplicants = [
        Duplicant("Kael", "Brute", 15, 12, 100, 0, 50),
        Duplicant("Lyra", "Éclaireur", 12, 8, 80, 0, 60),
        Duplicant("Ren", "Ingénieur", 8, 10, 90, 10, 40),
        Duplicant("Zara", "Chimiste", 10, 9, 70, 15, 55)
    ]
    return duplicants