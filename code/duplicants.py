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
        print(f"Nom: {self.nom}, Classe: {self.classe}")
        print(f"  ATT: {self.attaque}, DEF: {self.defense}, PV: {self.vie}, SOI: {self.soin}, STR: {self.stress}")
        print(f"  Inventaire: {', '.join(self.inventaire) if self.inventaire else 'Vide'}")
        print("  Compétences:")
        if self.competences:
            for i, competence in enumerate(self.competences):
                print(f"    {i + 1}. {competence['nom']} ({competence['type']})")
        else:
            print("    Aucune")