import random

def createEmptyDico(n):
    dico = {}
    for i in range(n):
        dico[i] = ""
    return dico

"""
fonction qui compare les dico et retourne le nombre de couleurs correctes
et de couleurs partiellement correctes
"""
def compare(dico1, dico2, colors):
    correct = 0
    partial = 0
    dico1Colors = {}
    dico2Colors = {}
    for i in colors:
        dico1Colors[i] = 0
        dico2Colors[i] = 0
    for i in range(len(dico1)):
        #compte le nombre de couleur
        dico1Colors[dico1[i]] += 1
        dico2Colors[dico2[i]] += 1
        #si les couleurs sont les mêmes au même emplacement alors on ajoute une couleur correcte
        if(dico1[i] == dico2[i]):
            correct += 1
    for i in range(len(dico1)):
        #si une couleur est présente dans les 2 dico alors on l'ajoute dans les partiels
        if(dico1Colors[dico1[i]] > 0 and dico2Colors[dico1[i]] > 0):
            partial += 1
            #on la retire pour éviter les faux doublons 
            dico2Colors[dico1[i]] -= 1
    partial -= correct
    return {"correct" : correct, "partial" : partial}
           
"""
fonction qui ouvre un fichier et qui retourne les données en tableau
"""     
def readFile(f):
    file = open(f, "r")
    data = file.readlines()
    data[0] = int(data[0].strip("\n"))
    data[1] = int(data[1])
    file.close()       
    return data

"""
fonction qui ecrit dans un fichier
"""
def writeFile(f, score, nParties):
    file = open(f, "w")
    file.write(str(score) + "\n" + str(nParties))
    file.close()

#constantes
colors = ["R", "V", "B", "J", "M", "N"]
maxTries = 12
colorNumber = 4

#programme principal
running = True
while(running):
    mode = input("Jouer(1)\nRéinitialiser les stats(2)\nQuitter(Appuyer sur n'importe quelle touche)\n")
    
    #mode jouer
    if(mode == '1'):
        play = True
        while(play):
            
            #chargement des stats
            data = readFile(".stats.txt")
            nParties = data[0]
            score = data[1]
            print("Vous avez joué " + str(nParties) + " parties\nVotre score total est " + str(score))
            
            print('Les couleurs sont : ' + str(colors))
            code = createEmptyDico(colorNumber)
            #tire le code au hasard parmi les couleurs de la liste
            for i in range(colorNumber):
                code[i] = random.choice(colors)
            print(code)
            
            guessStr = ""
            guessDico = createEmptyDico(colorNumber)
            tries = 0
            
            #jeu
            while(guessDico != code and tries <= maxTries):   
                tries += 1
                guessStr = input("Choisir un code (XXXX)\n")
                #transforme le string en dico
                for i in range(colorNumber):
                    guessDico[i] = guessStr[i]
                hint = compare(code, guessDico, colors)
                print("Correct : " + str(hint["correct"]) + " | Partiel : " + str(hint["partial"]))
                if(guessDico == code):
                    print("Trouvé en " + str(tries))
            
            #ecriture des stats
            nParties += 1
            score += maxTries - tries
            writeFile(".stats.txt", nParties, score)
            print("Vous avez joué " + str(nParties) + " parties\nVotre score total est " + str(score))
                    
            answer = input("Voulez vous rejouer ? o/n\n")
            if(answer != 'o'):
                play = False
        
    #mode réinitialiser
    if(mode == '2'):
        writeFile(".stats.txt", 0, 0)
        
    #quitter
    else:
        running = False