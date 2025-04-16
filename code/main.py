import random  # Importez le module random en haut du fichier
from duplicants import creer_duplicants # Si vous mettez les classes dans un fichier séparé

def afficher_aide():
    print("Commandes disponibles:")
    print("  help - Affiche cette aide")
    print("  exit - Quitte le jeu")
    print("  explorer - Commence l'exploration")
    print("  inventaire - Affiche l'inventaire")
    print("  sauvegarder - Sauvegarde la partie (bientôt disponible)")
    print("  duplicants - Affiche les détails des Duplicants")

def explorer(duplicants): # Accepter la liste des Duplicants
    print("Vous entrez dans un nouveau niveau...")
    print("L'air est lourd et humide, et des ombres dansent sur les murs.")
    print("Un faible écho résonne au loin.")

    # Événement aléatoire
    evenement = random.randint(1, 10)  # Augmenter la plage pour moins d'événements
    if evenement == 1:
        print("Vous entendez un bruit de chute derrière vous, mais vous ne voyez rien.")
    elif evenement == 2:
        print("Une légère brise vous frôle, vous donnant la chair de poule.")
    elif evenement == 3:
        print("Vous trouvez une petite pierre brillante sur le sol.")
    elif evenement == 4:  # Nouvelle condition pour le combat
        print("Soudain, une créature surgit devant vous!")
        creature = {"nom": "Hatchling", "niveau": 1, "type": "Base"}  # Créature simple pour commencer
        combat(duplicants, creature) # Lancer le combat
    elif evenement == 4:
        print("Soudain, une créature surgit devant vous!")
        creatures = [
            {"nom": "Hatchling", "niveau": 1, "type": "Base"},
            {"nom": "Lombricule", "niveau": 2, "type": "Acide"},
            {"nom": "Morb", "niveau": 3, "type": "Toxique"}
        ]
        creature = random.choice(creatures) # Choisir une créature aléatoirement
        combat(duplicants, creature)

    print("Où voulez-vous aller ?")
    print("1. Aller à gauche (un couloir étroit et sombre)")
    print("2. Aller tout droit (une grande salle ouverte)")
    print("3. Aller à droite (un chemin avec des marques étranges sur le sol)")
    choix = input("Entrez votre choix (1, 2 ou 3): ")
    if choix == "1":
        print("Vous vous engagez dans le couloir étroit. L'obscurité vous enveloppe...")
        # Logique pour la gauche
    elif choix == "2":
        print("Vous entrez dans la grande salle. Elle semble vide, mais vous avez un mauvais pressentiment...")
        # Logique pour tout droit
    elif choix == "3":
        print("Vous suivez le chemin marqué. Les marques semblent anciennes et mystérieuses...")
        # Logique pour la droite
    else:
        print("Choix invalide.")

def combat(duplicants, creature):
    print(f"\n--- Combat engagé contre {creature['nom']} (Niveau {creature['niveau']}) ---")
    print("Vos Duplicants attaquent!")
    for duplicant in duplicants:
        print(f"{duplicant.nom} attaque {creature['nom']}!")
    print(f"Vous infligez des dégâts à {creature['nom']}!")
    print(f"{creature['nom']} est vaincu!")
    print("--- Fin du combat ---")

def main():
    print("Bienvenue dans Galactic Scavengers : L'Ascension des Duplicants!")
    print("Vous êtes au Portal, le point de départ de votre aventure.")

    duplicants = creer_duplicants()  # Crée les Duplicants

    while True:
        commande = input("> ")
        if commande == "help":
            afficher_aide()
        elif commande == "exit":
            print("Merci d'avoir joué!")
            break
        elif commande == "explorer":
            explorer(duplicants) # Passer les Duplicants à explorer
        elif commande == "inventaire":
            print("Votre inventaire est vide.")
        elif commande == "sauvegarder":
            print("Fonctionnalité de sauvegarde à venir...")
        elif commande == "duplicants":
            print("\nVotre équipe de Duplicants:")
            for i, duplicant in enumerate(duplicants):
                print(f"{i + 1}. {duplicant.nom} ({duplicant.classe})")
            choix = input("Entrez le numéro du Duplicant pour voir ses détails (ou '0' pour revenir): ")
            if choix.isdigit():
                choix_index = int(choix) - 1
                if 0 <= choix_index < len(duplicants):
                    duplicants[choix_index].afficher_infos()
                elif choix_index == -1:
                    print("Retour à l'écran principal.")
                else:
                    print("Choix invalide.")
            else:
                print("Choix invalide.")
        else:
            print("Commande inconnue. Tapez 'help' pour obtenir de l'aide.")

if __name__ == "__main__":
    main()
