from pathlib import Path
from pprint import pprint

chemin = Path.home() / "Test.txt"

with open(chemin,'r') as f : 
    Contenu = f.read().splitlines()

prenoms= []

for line in Contenu : 
    prenoms.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

with open(chemin, "w") as f :
    f.write("\n".join(sorted(prenoms_final)))

with open(chemin, "r") as f : 
    a = f.read()
    print(a)