import random

ale = str(random.randint(1, 100))
f
i = 0

while i<=4 : 
    print(f"Il te reste {5-i} essais")
    a = input("Quel nombre avez-vous choisi ? : ")
    
    if a.isalpha():
        print("Veuillez entrer un nombre valable")
    elif a != ale :
        print("Ce n'est pas le bon résultat, courage !")
    elif a == ale :
        print("C'est le bon résultat GG !")
        print("A bientôt")
        break
    if a < ale : 
        print("C'est plus grand")
    elif a > ale : 
        print("C'est plus petit")
    if i == 4 : 
        print("A bientôt")
    i+= 1
    
    print("-" * 50)    