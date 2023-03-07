mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_court = ("Votre mot de passe est trop court.")
if len(mdp)==0:
    print(mdp_court.upper())
elif len(mdp)<8:
    print(mdp_court.capitalize())
elif mdp.isdigit() :
    print ("Votre mot de passe contient que des nombres")
elif mdp.isalpha() :
    print ("Votre mot de passe contient que des lettres")
else :
    print("Inscription terminée")    
