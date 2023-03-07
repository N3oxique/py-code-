import sys 

liste = []

Menu = """Que voulez vous faire  ? :
1 : Ajouter un élève  :
2 : Retirer un élève  : 
3 : Lister les élèves :
4 : Vider la liste    :
5 : Quitter           :

Vous choisissez : """

Choices = ["1", "2", "3", "4", "5"]

while True : 
    user_choice = ""
    while user_choice not in Choices :
        user_choice = input(Menu)
        if user_choice not in Choices :
            print("Veuillez choisir une option valide")
    
    if user_choice == "1": 
        student = input("Quel est le nom de l'élève ? : ")
        liste.append(student.capitalize)
        print(f"L'élève {student.capitalize} à bien été ajouté à la liste")         
    elif user_choice == "2":
        student_remove = input("Quel élève voulez-vous retirer ? : ")
        if student_remove in liste :
            liste.remove(student_remove)
            print(f"L'élève {student_remove} à été retirer de la liste.")
        else :
            print(f"L'élève n'est pas dans la liste.")
    elif user_choice == "3":
        print("Voici la liste :")
        for i, student in enumerate(liste, 1):
            print(f"{i}. {student}")
        else : 
            ("Votre liste ne contient rien.")
    elif user_choice == "4":
        liste.clear()
        if liste == "" :
            print("La liste à été vidée.")
        else :
            print("La liste est déjà vide.")
    elif user_choice == "5":
        print("Salut !")
        sys.exit()
    
    print("-"*100)

