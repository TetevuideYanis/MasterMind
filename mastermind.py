import random

"""
fonction qui compare les dico et retourne le nombre de couleurs correctes
et de couleurs partiellement correctes
"""
def compare(dico1, dico2):
    correct = 0
    partial = 0
    dico1Colors = {"R" : 0, "V" : 0, "B" : 0, "J" : 0, "M" : 0, "N" : 0}
    dico2Colors = {"R" : 0, "V" : 0, "B" : 0, "J" : 0, "M" : 0, "N" : 0}
    for i in range(4):
        #compte le nombre de couleur
        dico1Colors[dico1[i]] += 1
        dico2Colors[dico2[i]] += 1
        #si les couleurs sont les mêmes au même emplacement alors on ajoute une couleur correcte
        if(dico1[i] == dico2[i]):
            correct += 1
    for i in range(4):
        #si une couleur est présente dans les 2 dico alors on l'ajoute dans les partiels
        if(dico1Colors[dico1[i]] > 0 and dico2Colors[dico1[i]] > 0):
            partial += 1
            #on la retire pour éviter les faux doublons 
            dico2Colors[dico1[i]] -= 1
    partial -= correct
    return {"correct" : correct, "partial" : partial}
                
            

colors = ["R", "V", "B", "J", "M", "N"]
print('Les couleurs sont : ' + str(colors))
code = {0 : "", 1 : "", 2 : "", 3 : ""}
#tire le code au hasard parmi les couleurs de la liste
for i in range(4):
    code[i] = random.choice(colors)
print(code)

guessStr = ""
guessDico = {0 : "", 1 : "", 2 : "", 3 : ""}
tries = 0

while(guessDico != code and tries <= 12):
    tries += 1
    guessStr = input("Choisir un code (XXXX)\n")
    #transforme le string en dico
    for i in range(4):
        guessDico[i] = guessStr[i]
    hint = compare(code, guessDico)
    print("Correct : " + str(hint["correct"]) + " | Partiel : " + str(hint["partial"]))
    if(guessDico == code):
        print("Trouvé en " + str(tries))