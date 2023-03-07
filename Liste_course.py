import sys

LISTE = []

MENU = """Choisissez parmi les options suivantes : 
1: Ajouter un élement à la liste
2: Retirer un élement
3: Afficher la liste
4: Vider la liste
5: Quitter
 Votre choix : """

MENU_CHOICE = ["1", "2", "3", "4", "5"]

while True : 
    user_choice = ""
    while user_choice not in MENU_CHOICE:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICE:
            print("Veuillez choisir une option valide...")

    if user_choice == "1": 
        item = input("Entrez un élément à ajouter : ")
        LISTE.append(item)
        print(f"L'élément {item} à bien été ajouté à la liste.")
    elif user_choice == "2": 
        item = input("Entrez un élément à retirer : ")
        if item in LISTE :
            LISTE.remove(item)
            print(f"L'élément {item} à bien été supprimé à la liste.") 
        else: 
            print(f"L'élément {item} n'est pas dans la liste.") 
    elif user_choice == "3":
        if LISTE:
            print("Voici le contenu de la liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient rien.")     
    elif user_choice == "4":
        LISTE.clear()
        print("La liste à été vidée.")  
    elif user_choice == "5": 
        print("à bientôt")
        sys.exit()

    print("-" * 50)    
