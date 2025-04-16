import random

def creer_creature():
    creatures = [
        {"nom": "Hatchling", "niveau": 1, "type": "Base", "attaque_speciale": None},
        {"nom": "Lombricule", "niveau": 2, "type": "Acide", "attaque_speciale": "Crachat acide"},
        {"nom": "Morb", "niveau": 3, "type": "Toxique", "attaque_speciale": "Nuage toxique"},
        {"nom": "Squelette", "niveau": 2, "type": "Osseux", "attaque_speciale": None},  # Nouvelle créature
        {"nom": "Gueule-à-Venin", "niveau": 3, "type": "Plante", "attaque_speciale": "Tentacules"}  # Nouvelle créature
    ]
    creature = random.choice(creatures)
    return creature