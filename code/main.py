import random
from combat import combat
from creatures import creer_creature
from duplicants import creer_duplicants, Duplicant  # Assurez-vous d'importer Duplicant

objets_possibles = ["Pierre étrange", "Herbe médicinale", "Fragment de métal", "Cristal bleu"]


def afficher_aide():
    print("Commandes disponibles:")
    print("  help - Affiche cette aide")
    print("  exit - Quitte le jeu")
    print("  explorer - Commence l'exploration")
    print("  inventaire - Affiche l'inventaire")
    print("  sauvegarder - Sauvegarde la partie (bientôt disponible)")
    print("  duplicants - Affiche les détails des Duplicants")
    print("  utiliser - Permet d'utiliser un objet de l'inventaire")


def explorer(duplicants):
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
        objet_trouve = random.choice(objets_possibles)
        print(f"Vous trouvez un(e) {objet_trouve}!")
        # Ajouter l'objet à l'inventaire d'un Duplicant (par exemple, le premier)
        duplicants[0].inventaire.append(objet_trouve)
    elif evenement == 4:  # Nouvelle condition pour le combat
        print("Soudain, une créature surgit devant vous!")
        creature = creer_creature()  # Obtenir une créature de creatures.py
        combat(duplicants, creature)  # Lancer le combat (de combat.py)

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
            explorer(duplicants)
        elif commande == "utiliser":
            print("\nUtiliser un objet")
            print("\nVotre équipe de Duplicants:")
            for i, duplicant in enumerate(duplicants):
                print(f"{i + 1}. {duplicant.nom} ({duplicant.classe})")
            choix_duplicant = input(
                "Entrez le numéro du Duplicant qui va utiliser un objet (ou '0' pour revenir): ")
            if choix_duplicant.isdigit():
                choix_duplicant_index = int(choix_duplicant) - 1
                if 0 <= choix_duplicant_index < len(duplicants):
                    if duplicants[choix_duplicant_index].inventaire:
                        print(f"\nInventaire de {duplicants[choix_duplicant_index].nom} :")
                        for i, objet in enumerate(duplicants[choix_duplicant_index].inventaire):
                            print(f"{i + 1}. {objet}")
                        choix_objet = input("Entrez le numéro de l'objet à utiliser : ")
                        if choix_objet.isdigit():
                            choix_objet_index = int(choix_objet) - 1
                            if 0 <= choix_objet_index < len(
                                    duplicants[choix_duplicant_index].inventaire):
                                print(
                                    f"Vous utilisez {duplicants[choix_duplicant_index].inventaire[choix_objet_index]}...")
                                #  Ajouter ici la logique d'utilisation de l'objet
                                del duplicants[choix_duplicant_index].inventaire[
                                    choix_objet_index]  # Supprimer l'objet de l'inventaire après utilisation
                            else:
                                print("Choix d'objet invalide.")
                        else:
                            print("Choix d'objet invalide.")
                    else:
                        print(f"{duplicants[choix_duplicant_index].nom} n'a rien dans son inventaire.")
                elif choix_duplicant_index == -1:
                    print("Retour à l'écran principal.")
                else:
                    print("Choix de Duplicant invalide.")
            else:
                print("Choix de Duplicant invalide.")

        elif commande == "inventaire":
            print("\nInventaire")
            print("\nVotre équipe de Duplicants:")
            for i, duplicant in enumerate(duplicants):
                print(f"{i + 1}. {duplicant.nom} ({duplicant.classe})")
            choix = input("Entrez le numéro du Duplicant pour voir son inventaire (ou '0' pour revenir): ")
            if choix.isdigit():
                choix_index = int(choix) - 1
                if 0 <= choix_index < len(duplicants):
                    print(
                        f"Inventaire de {duplicants[choix_index].nom} : {', '.join(duplicants[choix_index].inventaire) if duplicants[choix_index].inventaire else 'Vide'}")
                elif choix_index == -1:
                    print("Retour à l'écran principal.")
                else:
                    print("Choix invalide.")
            else:
                print("Choix invalide.")
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