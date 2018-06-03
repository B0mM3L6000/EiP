import pygame as pg
import time

#klappt nicht mehr bei 50x50
#zuviele rechenschritte für rekursion


#einlesen der datei:

tmp = "Labyrinth20x20.txt"
labdata = open(tmp,"r")

#einlesen der zeilen in 2d feld:

lab = []

for line in labdata:
    tmpzeile = []
    line = line.rstrip()
    for letter in line:
        tmpzeile.append(letter)
    lab.append(tmpzeile)
"""
for _ in range(len(lab)):
    print(lab[_])

for _ in range(len(lab)):
    del lab[_][len(lab[_])-1]
"""
#schließen der eingabedatei
labdata.close()

for _ in range(len(lab)):
    print(lab[_])

print(len(lab))
print(len(lab[0]))
#print (len(lab[0]))

#finde startpunkt:
def start(labyrinth):
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[0])):
            if labyrinth[i][j] == "S":
                startpoint = [i,j]
                #print("Startpunkt gefunden bei:", startpoint)
                return startpoint
                break

start = start(lab)
print(start)



#Finde Weg und speichere ihn ab:

def search(labyrinth, start_zeile, start_spalte, history, zaehler):
    ziel = False
    end = True
    zaehler += 1
    error = False
    history.append([start_zeile,start_spalte])
    #print("Aktuelles feld am start:", start_zeile, start_spalte)
    #print("Aktueller zahler:", zaehler)
    #print("Aktuelle history:", history)
    #erinnerung an feld eintragen:
    labyrinth[start_zeile][start_spalte] = "0"
    #print(start_zeile)
    #print(start_spalte)
    #checke norden:
    #check ob außerhalb des feldes:
    if start_zeile-1 >= 0:
        #print("test")
        #check ob ziel:
        if labyrinth[start_zeile-1][start_spalte] == "Z":
            ziel = True
            end = False
        #check obs weiter geht:
        elif labyrinth[start_zeile-1][start_spalte] == " ":
            #neu aufrufen
            #eintragen als (potentiellen weg)
            #labyrinth[start_zeile-1][start_spalte] = "W"
            print("nord")
            end = False
            labyrinth, error = search(labyrinth, start_zeile-1, start_spalte,history, zaehler)
            if labyrinth[start_zeile-1][start_spalte] == "Z":
                ziel = True
        #check ob wand oder alter weg oder sackgasse(also kein weiterer weg/ziel)
        #elif labyrinth[start_zeile][start_spalte] == "X" or =="W" or =="O":
            #abbruch
    if ziel != True:
        #print("test")
        #checke osten:
        if start_spalte+1 < len(labyrinth):
            #print("test2")
            #check ob ziel:
            if labyrinth[start_zeile][start_spalte+1] == "Z":
                ziel = True
                end = False
            #check obs weiter geht:
            elif labyrinth[start_zeile][start_spalte+1] == " ":
                #print("test")
                #neu aufrufen
                #eintragen als (potentiellen weg)
                #labyrinth[start_zeile][start_spalte+1] = "W"
                print("ost")
                end = False
                labyrinth, error = search(labyrinth, start_zeile, start_spalte+1,history, zaehler)
                if labyrinth[start_zeile][start_spalte+1] == "Z":
                    ziel = True
    #checke süden:
    if ziel != True:
        #checke osten:
        if start_zeile+1 < len(labyrinth[0]):
            #print("suedentest")
            #check ob ziel:
            if labyrinth[start_zeile+1][start_spalte] == "Z":
                ziel = True
                end = False
            #check obs weiter geht:
            elif labyrinth[start_zeile+1][start_spalte] == " ":
                #print("suedentest2")
                #neu aufrufen
                #eintragen als (potentiellen weg)
                #labyrinth[start_zeile+1][start_spalte] = "W"
                print("sued")
                end = False
                labyrinth, error = search(labyrinth, start_zeile+1, start_spalte,history, zaehler)
                if labyrinth[start_zeile+1][start_spalte] == "Z":
                    ziel = True

    #checke westen:
    if ziel != True:
        #checke osten:
        if start_spalte > 0:
            #print("westentest")
            #check ob ziel:
            if labyrinth[start_zeile][start_spalte-1] == "Z":
                ziel = True
                end = False
            #check obs weiter geht:
            elif labyrinth[start_zeile][start_spalte-1] == " ":
                #neu aufrufen
                #eintragen als (potentiellen weg)
                #labyrinth[start_zeile][start_spalte-1] = "W"
                print("west")
                end = False
                labyrinth, error = search(labyrinth, start_zeile, start_spalte-1,history, zaehler)
                if labyrinth[start_zeile][start_spalte-1] == "Z":
                    ziel = True
    #checken ob sackgasse und dann einen schritt zurück:
    if end == True:
        if history[zaehler-1] == "end":
            #print("nicht lösbar")
            error = True
        else:
            #print("sackgasse")
            #print("Aktuelles feld:", start_zeile, start_spalte)
            #for _ in range(len(labyrinth[0])):
            #    print(labyrinth[_])
            del history[zaehler]
            tmphistory = history[:]
            #print(tmphistory)
            del history[zaehler-1]
            #print(tmphistory)
            #print(history)
            #print("endetest")
            labyrinth, error = search(labyrinth,tmphistory[zaehler-1][0], tmphistory[zaehler-1][1],history, zaehler-2)
    #if ziel != True:
        #abbruch und als sackgasse eintragen
        #labyrinth[start_zeile][start_spalte] = "O"
    if ziel == True:
        labyrinth[start_zeile][start_spalte] = "Z"

    #ausgabe:
    return labyrinth, error




#male weg mit pygame:

def rendern(weg):
    #variablen für gitter und farben:
    zeilen = len(weg)
    spalten = len(weg[0])
    print(zeilen, spalten)
    black = [0,0,0]
    white = [255,255,255]
    red = [255,0,0]
    pixel = 10
    pg.init()
    pg.display.set_caption("Weg durchs Labyrinth")
    bildschirm = pg.display.set_mode((len(weg)*pixel,len(weg[0])*pixel))
    bildschirm.fill(white)
    for zeile in range(zeilen):
        for spalte in range(spalten):
            if weg[zeile][spalte] == "X":
                pg.draw.rect(bildschirm, black,(spalte*pixel,zeile*pixel,pixel, pixel))
            elif weg[zeile][spalte] == "Z":
                pg.draw.rect(bildschirm, red,(spalte*pixel,zeile*pixel,pixel, pixel))
    pg.display.flip()
    time.sleep(15)




#ausführen:
history = ["end"]
zaehler = 0
test, errormeldung = search(lab, start[0], start[1], history, zaehler)

if errormeldung == True:
    print("Das Labyrinth ist nicht loesbar.")
else:
    for _ in range(len(test[0])):
        print(test[_])


rendern(test)
