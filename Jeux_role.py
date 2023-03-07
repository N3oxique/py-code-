import sys 

import random

from random import randint

vie_j1 = 50
vie_j2 = 50
nbr_popo = 3


while vie_j1 or vie_j2 >=0 :

     atk_j1 = str(random.randint(5, 10))
     atk_j2 = str(random.randint(5, 15))
     atk_j22 = str(random.randint(5, 15))
     popo = str(random.randint(15, 50))

     print(f"""
     Il te reste {vie_j1} HP.
     Il reste {vie_j2} HP à ton ennemi.
     """)

     choix = input("Voulez-vous attaquer ou prendre une potion ? '1' ou '2' : ")
     
     if choix == "1" :
         print(f"Vous avez infligé -{atk_j1} HP !")
         print(f"Ton ennemi t'as infligé -{atk_j2} HP !")
         vie_j1 -= int(atk_j2)
         vie_j2 -= int(atk_j1)
     
     elif choix == "2":
          vie_j1 -= int(atk_j2)
          vie_j1 -= int(atk_j22)
          print(f"Ton ennemi t'as infligé -{atk_j2} HP et tu vas rien faire !")
          print(f"Ton ennemi t'as infligé -{atk_j22} HP pendant le tours passé !")
     
     else :
          choix 
    

     if choix == "2":
          vie_j1 += int(popo)
          if nbr_popo >0 :
               print(f"Vous utilisez une potion qui vous rend {popo} d'HP et passe votre prochain tours !")
               nbr_popo -= 1
          elif nbr_popo <= 0:
               print("Vous n'avez plus de potions")
               vie_j1 -= int(popo)
     
     if vie_j2 <= 0 : 
          print("Vous avez gagné !")
          break

     if vie_j1 <= 0 :
          print("Vous avez perdu !")
          break
    
     print("-" * 50)
    

