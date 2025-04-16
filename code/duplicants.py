class Duplicant:
    def __init__(self, nom, classe, attaque, defense, vie, soin, stress):
        self.nom = nom
        self.classe = classe
        self.attaque = attaque
        self.defense = defense
        self.vie = vie
        self.soin = soin
        self.stress = stress
        self.inventaire = []
        self.competences = self.definir_competences()  # Ajout des compétences

    def definir_competences(self):
        # Définir les compétences de base pour chaque classe
        if self.classe == "Brute":
            return ["Frappe puissante"]
        elif self.classe == "Éclaireur":
            return ["Tir rapide"]
        elif self.classe == "Ingénieur":
            return ["Construire tourelle"]
        elif self.classe == "Chimiste":
            return ["Jet acide"]
        else:
            return []

    def afficher_infos(self):
        print(f"Nom: {self.nom}, Classe: {self.classe}")
        print(f"  ATT: {self.attaque}, DEF: {self.defense}, PV: {self.vie}, SOI: {self.soin}, STR: {self.stress}")
        print(f"  Inventaire: {', '.join(self.inventaire) if self.inventaire else 'Vide'}")
        print(f"  Compétences: {', '.join(self.competences) if self.competences else 'Aucune'}")

def creer_duplicants():
    duplicants = [
        Duplicant("Kael", "Brute", 15, 12, 100, 0, 50),
        Duplicant("Lyra", "Éclaireur", 12, 8, 80, 0, 60),
        Duplicant("Ren", "Ingénieur", 8, 10, 90, 10, 40),
        Duplicant("Zara", "Chimiste", 10, 9, 70, 15, 55)
    ]
    return duplicants