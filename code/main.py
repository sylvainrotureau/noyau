def afficher_aide():
    print("Commandes disponibles:")
    print("  help - Affiche cette aide")
    print("  exit - Quitte le jeu")
    print("  explorer - Commence l'exploration")
    print("  inventaire - Affiche l'inventaire")
    print("  sauvegarder - Sauvegarde la partie (bientôt disponible)")

def explorer():
    print("Vous entrez dans un nouveau niveau...")
    print("Il fait sombre et vous entendez des bruits étranges.")
    print("Que voulez-vous faire ?")
    print("1. Avancer prudemment")
    print("2. Allumer votre lampe torche")
    choix = input("Entrez votre choix (1 ou 2): ")
    if choix == "1":
        print("Vous avancez lentement...")
    elif choix == "2":
        print("La lumière révèle un long couloir...")
    else:
        print("Choix invalide.")

def main():
    print("Bienvenue dans Galactic Scavengers : L'Ascension des Duplicants!")
    print("Vous êtes au Portal, le point de départ de votre aventure.")    
    while True:
        commande = input("> ")
        if commande == "help":
            afficher_aide()
        elif commande == "exit":
            print("Merci d'avoir joué!")
            break
        elif commande == "explorer":
            print("Vous commencez votre exploration...")
            # Logique d'exploration ici
        elif commande == "inventaire":
            print("Votre inventaire est vide.")
            # Logique d'inventaire ici
        elif commande == "explorer":
            explorer()
        elif commande == "sauvegarder":
            print("Fonctionnalité de sauvegarde à venir...") # À implémenter plus tard    
        else:
            print("Commande inconnue. Tapez 'help' pour obtenir de l'aide.")

if __name__ == "__main__":
    main()
