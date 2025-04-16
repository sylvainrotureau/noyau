import random

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
        self.competences = self.definir_competences()
        self.niveau = 1  # Niveau de départ
        self.experience = 0  # Expérience actuelle

    def definir_competences(self):
        if self.classe == "Brute":
            return [
                {"nom": "Frappe puissante", "type": "attaque", "puissance": 2.0, "effet": None},
            ]
        elif self.classe == "Éclaireur":
            return [
                {"nom": "Tir rapide", "type": "attaque", "puissance": 1.0, "effet": "defense_baisse"},
            ]
        elif self.classe == "Ingénieur":
            return [
                {"nom": "Construire tourelle", "type": "autre", "puissance": 0, "effet": None},
            ]
        elif self.classe == "Chimiste":
            return [
                {"nom": "Jet acide", "type": "attaque", "puissance": 1.5, "effet": "attaque_baisse"},
            ]
        else:
            return []

    def afficher_infos(self):
        print(f"Nom: {self.nom}, Classe: {self.classe}, Niveau: {self.niveau}")
        print(f"  ATT: {self.attaque}, DEF: {self.defense}, PV: {self.vie}, SOI: {self.soin}, STR: {self.stress}")
        print(f"  Inventaire: {', '.join(self.inventaire) if self.inventaire else 'Vide'}")
        print("  Compétences:")
        if self.competences:
            for i, competence in enumerate(self.competences):
                print(f"    {i + 1}. {competence['nom']} ({competence['type']})")
        else:
            print("    Aucune")

    def gagner_experience(self, xp):
        self.experience += xp
        print(f"{self.nom} gagne {xp} points d'expérience!")
        self.verifier_niveau_up()

    def verifier_niveau_up(self):
        niveau_suivant = 100 * self.niveau  # Exemple : 100 XP par niveau
        if self.experience >= niveau_suivant:
            self.niveau_up()

    def niveau_up(self):
        self.niveau += 1
        self.attaque += random.randint(1, 3)
        self.defense += random.randint(1, 2)
        self.vie += random.randint(5, 10)
        self.soin += random.randint(0, 2)
        self.stress -= random.randint(0, 5)  # Réduire le stress au niveau up
        print(f"\n{self.nom} monte au niveau {self.niveau}!")
        print(f"Ses statistiques augmentent!")
        self.afficher_infos()