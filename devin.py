import random

def joueur_devine():
    '''
    Jeu du devin où la machine fait deviner le nombre
    La machine choisit un nombre et le fait deviner à l'utilisateur.
    '''

    # Déterminer un nombre compris entre 1 et 999            
    nombre = random.randint(1, 999)
    print("J'ai choisi un nombre compris entre 1 et 999.")

    # Faire deviner ce nombre
    found = False
    nb_essai = 0
    while not found:
        # Faire deviner une fois ce nombre
        #   Demander une proposition à l'utilisateur
        nb_essai += 1
        proposition = input('Proposition {} : '.format(nb_essai))
        while not proposition.isdigit():
            proposition = input('Proposition {} : '.format(nb_essai))
        proposition = int(proposition)

        #   Évaluer cette proposition utilisateur
        if proposition < nombre:
            print('Trop petit')
        elif proposition > nombre:
            print('Trop grand')
        else:
            found = True
            print('Trouvé !')
    
    # Annoncer le résultat
    print('Bravo ! Vous avez trouvé le nombre en {} essai(s)'.format(nb_essai))
    print()


def machine_devine():
    '''
    Jeu du devin où la machine devine le nombre
    L'utilisateur choisit un nombre et la machine doit le trouver. Pour chaque nombre proposé par la machine, l'utilisateur indique s'il est trop petit ('p' ou 'P'), trop grand ('g' ou 'G') ou trouvé ('t', 'T')
    '''

    # Demander à l'utilisateur de choisir un nombre compris entre 1 et 999         
    ready = False
    while not ready:
        pret = input('Avez-vous choisi un nombre compris entre 1 et 999 (o/n) ? ').lower()
        if pret != 'o':
            print("J'attends…")
        else:
            ready = True
        
    # Trouver le nombre de l’utilisateur
    nb_essai = 0
    found = False

    #   Définir les limites du choix machine
    debut, fin = 1, 999

    while not found:
        #   Calculer un choix machine
        choix = int((debut + fin) // 2)
        nb_essai += 1

        #   Afficher le choix machine
        print('Proposition {} : {}'.format(nb_essai, choix))

        #   Demander à l'utilisateur d'évaluer le choix
        eval = input("Trop (g)rand, trop (p)etit ou (t)rouvé ? ").lower()
        while eval not in ('g', 'p', 't'):
            print("Je n'ai pas compris la réponse. Merci de répondre")
            print("g si ma proposition est trop grande")
            print("p si ma proposition est trop petite")
            print(" t si j'ai trouvé le nombre")
            eval = input("Trop (g)rand, trop (p)etit ou (t)rouvé ? ").lower()
        
        #   Traiter l’évaluation utilisateur	
        if eval == "g":
            fin = choix
        elif eval == "p":
            debut = choix
        else:
            found = True

    # Annoncer le résultat
    print("J'ai trouvé en {} essai(s)".format(nb_essai))
    print()


def choisir_jeu():
    '''
    Demander à l'utilisateur à quel jeu du devin il souhaite jouer
    1- L'ordinateur choisit un nombre et vous le devinez
    2- Vous choisissez un nombre et l'ordinateur le devine
    0- Quitter le programme
    '''

    play = True 
    while play:
        # Afficher menu
        print("1- L'ordinateur choisit un nombre et vous le devinez")
        print("2- Vous choisissez un nombre et l'ordinateur le devine")
        print("0- Quitter le programme")
        
        # Demander le choix utilisateur
        choix = input('''Votre choix : ''')
        print()
        
        # Lancer le jeu choisi
        if choix == '1':
            joueur_devine()
        elif choix == '2':
            machine_devine()
        else:
            play = False
    
    print("Au revoir...")


if __name__ == '__main__':
    choisir_jeu()
