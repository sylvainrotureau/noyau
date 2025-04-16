import random

def creer_creature():
    creatures = [
        {"nom": "Hatchling", "niveau": 1, "type": "Base"},
        {"nom": "Lombricule", "niveau": 2, "type": "Acide"},
        {"nom": "Morb", "niveau": 3, "type": "Toxique"}
    ]
    creature = random.choice(creatures)  # Choisir une créature aléatoirement
    return creature