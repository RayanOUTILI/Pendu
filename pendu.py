import csv
import random
import time
#indiquer le chemin courant avec un cd

def importdepuiscsv():
    global listemot
    listemot=[]
    nomfichier="listemots.csv"
    with open(nomfichier, 'r', newline='') as fichier:
        reader = csv.reader(fichier)
        for ligne in reader:
            listemot.append(ligne)

def afficheListe(liste):
    text=""
    for i in liste:
        text=text+i+" "
    print(text)
def etape0():
    print(" ")
    time.sleep(0.1)
    print(" ")
    time.sleep(0.1)
    print(" ")
    time.sleep(0.1)
    print(" ")
    time.sleep(0.1)
    print(" ")
    time.sleep(0.1)
    print(" ")
    time.sleep(0.1)
    print("=============")
    time.sleep(0.2)
def etape1():
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("=============")
    time.sleep(0.2)
def etape2():
    print("+-------+")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("=============")
    time.sleep(0.2)
def etape3():
    print("+-------+")
    time.sleep(0.1)
    print("|/      |")
    time.sleep(0.1)
    print("|        ")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("=============")
    time.sleep(0.2)
def etape4():
    print("+-------+")
    time.sleep(0.1)
    print("|/      |")
    time.sleep(0.1)
    print("|       O")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("=============")
    time.sleep(0.2)
def etape5():
    print("+-------+")
    time.sleep(0.1)
    print("|       |")
    time.sleep(0.1)
    print("|       O")
    time.sleep(0.1)
    print("|       |")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("=============")
    time.sleep(0.2)
def etape6():
    print("+-------+")
    time.sleep(0.1)
    print("|       |")
    time.sleep(0.1)
    print("|       O")
    time.sleep(0.1)
    print("|      -|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("=============")
    time.sleep(0.2)
def etape7():
    print("+-------+")
    time.sleep(0.1)
    print("|       |")
    time.sleep(0.1)
    print("|       O")
    time.sleep(0.1)
    print("|      -|-")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("=============")
    time.sleep(0.2)
def etape8():
    print("+-------+")
    time.sleep(0.1)
    print("|       |")
    time.sleep(0.1)
    print("|       O")
    time.sleep(0.1)
    print("|      -|-")
    time.sleep(0.1)
    print("|      |")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("=============")
    time.sleep(0.2)
def etape9():
    print("+-------+")
    time.sleep(0.1)
    print("|       |")
    time.sleep(0.1)
    print("|       O ")
    time.sleep(0.1)
    print("|      -|-")
    time.sleep(0.1)
    print("|      | |")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("=============")
    time.sleep(0.2)
def etape10():
    print("+-------+")
    time.sleep(0.1)
    print("|       |")
    time.sleep(0.1)
    print("|     \ O /")
    time.sleep(0.1)
    print("|      -|-")
    time.sleep(0.1)
    print("|      | |")
    time.sleep(0.1)
    print("|")
    time.sleep(0.1)
    print("=============")
    time.sleep(0.2)

def pendu():
    importdepuiscsv()
    mot=random.choice(listemot[random.randint(0,25)])
    texte=[]
    mottrouvé=[]
    lettresénoncées=[]
    for i in mot:
        texte.append("_")
    essais=input("Bonjour veuillez choisir la difficulté (elle aura un impact sur votre nombre de vies); facile ou difficile ?")
    if essais=="facile":
        nbessais=10
        print(" ")
        print("Niveau bien pris en compte !")
    elif essais=="difficile":
        nbessais=6
        print(" ")
        print("Niveau bien pris en compte !")
    elif essais != "facile" or "difficile":
        print(" ")
        print("ERREUR, on a dit facile ou difficile, vous aurez donc le niveau facile !")
        essais="facile"
        nbessais=10
    time.sleep(4)
    print(" ")
    print("Un mot a automatiquement été choisi, vos propositions seront affichées sous le mot à deviner,bonne chance !")
    time.sleep(8) #à décommenter à la fin
    for i in range(10):
        print(" ")
    print("Voici votre pendu pour le moment :")
    if essais=="difficile":
        etape1()
    else:
        etape0()
    time.sleep(3)
    afficheListe(texte)
    while nbessais!=0:
        if essais=="facile":
            if nbessais<10:
                print(mottrouvé)
        elif essais=="difficile":
            if nbessais<6:
                print(mottrouvé)
        lettre1=input("Veuillez entrer une lettre: ")
        print(" ")
        lettresénoncées.append(lettre1)
        if lettre1 in mot:
            print("Bien joué !")
            print("Il vous reste :",nbessais,"essais")
            print(lettresénoncées)
            for i in range(len(mot)):
                if mot[i]==lettre1:
                    texte.pop(i)
                    texte.insert(i,lettre1)
                    mottrouvé = ' '.join(texte)
            if nbessais==10:
                print(mottrouvé)
            if "_" not in mottrouvé:
                print(" ")
                print(" ")
                print("Bravo ! Vous avez gagné, il s'agissait bien du mot "+mot+".")
                break
        else:
            if len(lettre1)>1:
                print("Attention, qu'une seule lettre est demandée !")
                time.sleep(1)
            nbessais-=1
            print("Cette lettre n'est pas dans le mot, il vous reste plus que:",nbessais,"essais")
            time.sleep(1)
            if nbessais==9:
                etape1()
            elif nbessais==8:
                etape2()
            elif nbessais==7:
                etape3()
            elif nbessais==6:
                etape4()
            elif nbessais==5:
                if essais=="difficile":
                    etape3()
                else:
                    etape5()
            elif nbessais==4:
                if essais=="difficile":
                    etape4()
                else:
                    etape6()
            elif nbessais==3:
                if essais=="difficile":
                    etape6()
                else:
                    etape7()
            elif nbessais==2:
                if essais=="difficile":
                    etape7()
                else:
                    etape8()
            elif nbessais==1:
                if essais=="difficile":
                    etape8()
                else:
                    etape9()
            elif nbessais==0:
                if essais=="difficile":
                    etape9()
                else:
                    etape10()
                print("Vous avez perdu, le mot était "+mot)
                break
            print(lettresénoncées)
