import random
from duplicants import Duplicant

def combat(duplicants, creature):
    print(f"\n--- Combat engagé contre {creature['nom']} (Niveau {creature['niveau']}) ---")

    # Initialiser les PV et la défense
    for duplicant in duplicants:
        duplicant.vie = duplicant.vie
    creature_pv = 50 * creature['niveau']
    creature_defense = creature['niveau'] * 2
    creature_attaque = creature['niveau'] * 3 # Ajout de l'attaque de la créature de base
    effets_creature = {} # Dictionnaire pour stocker les effets sur la créature

    print(f"{creature['nom']} a {creature_pv} PV, {creature_defense} DEF et {creature_attaque} ATT.")

    tour = 1
    while creature_pv > 0 and any(duplicant.vie > 0 for duplicant in duplicants):
        print(f"\n--- Tour {tour} ---")
        creature_pv = tour_joueur(duplicants, creature, creature_attaque, creature_defense, creature_pv, effets_creature) # Ajout de creature_attaque et effets_creature
        if creature_pv > 0:
            tour_creature(duplicants, creature, effets_creature) # Passage de effets_creature
        tour += 1

    if creature_pv <= 0:
        print(f"\nVous avez vaincu {creature['nom']}!")
    else:
        print("\nVos Duplicants ont été vaincus...")
        print("Le Portal attend votre prochaine équipe.")
    print("--- Fin du combat ---")


def tour_joueur(duplicants, creature, creature_attaque_base, creature_defense, creature_pv, effets_creature): # Ajout de creature_attaque_base et effets_creature
    print("\n-- Tour des Duplicants --")
    for duplicant in duplicants:
        if duplicant.vie > 0:
            print(f"\n{duplicant.nom} ({duplicant.classe}) agit.")
            print("Choisissez une action :")
            print("1. Attaque de base")
            if duplicant.competences:
                for i, competence in enumerate(duplicant.competences):
                    print(f"{i + 2}. {competence['nom']}")
            choix = input("Entrez le numéro de l'action : ")
            if choix == "1":
                degats = duplicant.attaque - creature_defense
                if degats < 0:
                    degats = 0
                print(f"{duplicant.nom} attaque {creature['nom']} et inflige {degats} dégâts.")
            elif choix.isdigit() and int(choix) >= 2 and int(choix) <= len(duplicant.competences) + 1:
                choix_competence = int(choix) - 2
                degats = utiliser_competence(duplicant, duplicant.competences[choix_competence], creature, effets_creature) # Passage de effets_creature
            else:
                print("Choix invalide. Attaque de base utilisée.")
                degats = duplicant.attaque - creature_defense
                if degats < 0:
                    degats = 0
                print(f"{duplicant.nom} attaque {creature['nom']} et inflige {degats} dégâts.")
            creature_pv -= degats
            return creature_pv
    return creature_pv


def utiliser_competence(duplicant, competence, creature, effets_creature): # Passage de effets_creature
    if competence["nom"] == "Frappe puissante":
        degats = int(duplicant.attaque * competence["puissance"]) - creature['niveau']
        if degats < 0:
            degats = 0
        print(f"{duplicant.nom} utilise Frappe puissante et inflige {degats} dégâts!")
        return degats
    elif competence["nom"] == "Tir rapide":
        degats = duplicant.attaque - creature['niveau']
        if degats < 0:
            degats = 0
        print(f"{duplicant.nom} utilise Tir rapide et inflige {degats} dégâts!")
        # Appliquer l'effet (baisse de défense)
        effets_creature["defense_baisse"] = 1 # Indique que l'effet est actif
        print(f"La défense de {creature['nom']} est réduite!")
        return degats
    elif competence["nom"] == "Construire tourelle":
        print(f"{duplicant.nom} tente de construire une tourelle (Fonctionnalité non implémentée)!")
        return 0
    elif competence["nom"] == "Jet acide":
        degats = int(duplicant.attaque * competence["puissance"]) - creature['niveau']
        if degats < 0:
            degats = 0
        print(f"{duplicant.nom} utilise Jet acide et inflige {degats} dégâts!")
        # Appliquer l'effet (baisse d'attaque)
        effets_creature["attaque_baisse"] = 1 # Indique que l'effet est actif
        print(f"L'attaque de {creature['nom']} est réduite!")
        return degats
    else:
        print(f"{duplicant.nom} tente d'utiliser une compétence inconnue!")
        return 0


def tour_creature(duplicants, creature, effets_creature): # Passage de effets_creature
    print(f"\n-- Tour de {creature['nom']} --")

    # Calculer l'attaque de la créature en tenant compte des effets
    attaque_creature = creature['niveau'] * 3
    if "attaque_baisse" in effets_creature:
        attaque_creature = int(attaque_creature * 0.8) # Réduire l'attaque de 20%

    duplicant_cible = random.choice([d for d in duplicants if d.vie > 0])
    attaque_choix = random.randint(1, 2)
    if attaque_choix == 1:
        degats = attaque_creature # Utiliser l'attaque modifiée
        print(f"{creature['nom']} attaque {duplicant_cible.nom} et inflige {degats} dégâts.")
    elif attaque_choix == 2:
        degats = int(attaque_creature * 0.7) # Utiliser l'attaque modifiée
        print(f"{creature['nom']} tente une attaque rapide sur {duplicant_cible.nom} et inflige {degats} dégâts.")
    else:
        degats = attaque_creature
        print(f"{creature['nom']} attaque {duplicant_cible.nom} et inflige {degats} dégâts.")
    duplicant_cible.vie -= degats
    print(f"{duplicant_cible.nom} a maintenant {duplicant_cible.vie} PV.")
    if duplicant_cible.vie <= 0:
        print(f"{duplicant_cible.nom} est mort!")

    # Retirer les effets (pour l'instant, ils durent un tour)
    effets_creature.clear()