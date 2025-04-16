import random
from duplicants import Duplicant  # Assurez-vous d'importer Duplicant

def combat(duplicants, creature):
    print(f"\n--- Combat engagé contre {creature['nom']} (Niveau {creature['niveau']}) ---")

    # Initialiser les PV
    for duplicant in duplicants:
        duplicant.vie = duplicant.vie  # Réinitialiser les PV au max (ou garder les PV actuels)
    creature_pv = 50 * creature['niveau']  # Exemple : PV de la créature = 50 * niveau

    print(f"{creature['nom']} a {creature_pv} PV.")

    tour = 1
    while creature_pv > 0 and any(duplicant.vie > 0 for duplicant in duplicants):
        print(f"\n--- Tour {tour} ---")
        creature_pv = tour_joueur(duplicants, creature, creature_pv)
        if creature_pv > 0:
            tour_creature(duplicants, creature)
        tour += 1

    if creature_pv <= 0:
        print(f"\nVous avez vaincu {creature['nom']}!")
    else:
        print("\nVos Duplicants ont été vaincus...")
        print("Le Portal attend votre prochaine équipe.")  # Message temporaire
    print("--- Fin du combat ---")

def tour_joueur(duplicants, creature, creature_pv):
    print("\n-- Tour des Duplicants --")
    for duplicant in duplicants:
        if duplicant.vie > 0:
            print(f"\n{duplicant.nom} ({duplicant.classe}) agit.")
            print("Choisissez une action :")
            print("1. Attaque de base")  # Pour l'instant, c'est la seule option
            choix = input("Entrez le numéro de l'action : ")
            if choix == "1":
                degats = duplicant.attaque - creature['niveau']  # Exemple de calcul de dégâts
                if degats < 0:
                    degats = 0
                print(f"{duplicant.nom} attaque {creature['nom']} et inflige {degats} dégâts.")
                creature_pv -= degats
                return creature_pv
            else:
                print("Choix invalide. Attaque de base utilisée.")
                degats = duplicant.attaque - creature['niveau']
                if degats < 0:
                    degats = 0
                print(f"{duplicant.nom} attaque {creature['nom']} et inflige {degats} dégâts.")
                creature_pv -= degats
                return creature_pv
    return creature_pv

def tour_creature(duplicants, creature):
    print(f"\n-- Tour de {creature['nom']} --")
    duplicant_cible = random.choice([d for d in duplicants if d.vie > 0])  # Cibler un Duplicant vivant au hasard
    attaque_choix = random.randint(1, 2)
    if attaque_choix == 1:
        degats = creature['niveau'] * 2  # Attaque normale
        print(f"{creature['nom']} attaque {duplicant_cible.nom} et inflige {degats} dégâts.")
    elif attaque_choix == 2:
        degats = creature['niveau']  # Attaque faible
        print(f"{creature['nom']} tente une attaque rapide sur {duplicant_cible.nom} et inflige {degats} dégâts.")
    else:
        degats = creature['niveau']
        print(f"{creature['nom']} attaque {duplicant_cible.nom} et inflige {degats} dégâts.")
    duplicant_cible.vie -= degats
    print(f"{duplicant_cible.nom} a maintenant {duplicant_cible.vie} PV.")
    if duplicant_cible.vie <= 0:
        print(f"{duplicant_cible.nom} est mort!")