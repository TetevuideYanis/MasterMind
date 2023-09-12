import random


            

colors = ["R", "V", "B", "J", "M", "N"]
print('Les couleurs sont : ' + str(colors))
code = {0 : "", 1 : "", 2 : "", 3 : ""}
#tire le code au hasard parmi les couleurs de la liste
for i in range(4):
    code[i] = random.choice(colors)

guessStr = ""
guessDico = {0 : "", 1 : "", 2 : "", 3 : ""}
tries = 0

while(guessDico != code and tries <= 12):
    tries += 1
    guessStr = input("Choisir un code (XXXX)\n")
    #transforme le string en dico
    for i in range(4):
        guessDico[i] = guessStr[i]
    if(guessDico == code):
        print("Trouvé en " + str(12 - tries))