import pygame as pg

"""

Höhe mal Breite: 6x7
4 gleiche Steine aneinander diagonalrunter/diagonalhoch/horizontal/vertikal gewinnt
beide Spieler ziehen nacheinander
wählen eine spalte und der stein wird dann auf den untersten freien spaltenplatz gesetzt
nach jedem stein überprüfen, ob ein spieler gewonnen hat

"""

def initialisieren():
    spielfeld = list()
    for i in range(6):
        zeile = [0]*7
        spielfeld.append(zeile)
    return spielfeld


def wincheck(spielfeld, spieler):
    testfeld = spielfeld
    gewonnen = False
    #checken für jede zeile
    for i in range(5,-1,-1):
        #ob 4 in einer reihe nacheinander gleich sind
        zaehler = 0
        for j in range(7):
            if testfeld[i][j] == spieler:
                zaehler +=1
                if zaehler == 4:
                    gewonnen = True
                    break
            else:
                zaehler = 0

    #checken für jede spalte
    for i in range(7):
        zaehler = 0
        for j in range(5,-1,-1):
            if testfeld[j][i] == spieler:
                zaehler +=1
                if zaehler == 4:
                    gewonnen = True
                    break
            else:
                zaehler = 0

    #checken für jede diagonalerunter
    for i in range (6):
        for j in range(7):
            zaehler = 0
            for k in range(6):
                if j+k > 6 or i+k >5:
                    #print(i+k, j+k, "out of bounds")
                    zaehler = 0
                    break
                else:
                    #print(i+k, j+k, "Feldwert:", testfeld[i+k][j+k])
                    if testfeld[i+k][j+k] == spieler:
                        zaehler +=1
                        #print(zaehler)
                        if zaehler == 4:
                            gewonnen = True
                            #print("gewonnen")
                    else:
                        zaehler = 0
                        #print(zaehler)
            else:
                continue

    #checken für jede diagonalhoch
    for i in range (6):
        for j in range(7):
            zaehler = 0
            for k in range(6):
                if j+k > 6 or i-k <0:
                    #print(i+k, j+k, "out of bounds")
                    zaehler = 0
                    break
                else:
                    #print(i+k, j+k, "Feldwert:", testfeld[i+k][j+k])
                    if testfeld[i-k][j+k] == spieler:
                        zaehler +=1
                        #print(zaehler)
                        if zaehler == 4:
                            gewonnen = True
                            #print("gewonnen")
                    else:
                        zaehler = 0
                        #print(zaehler)
            else:
                continue

    return gewonnen


def action():
    #aktion für aktuellen spieler ermöglichen + rendern
    fehler = True
    while fehler == True:
        action = int(input("Welche Spalte (0-6)?"))
        if action >=0 and action <=6:
            fehler = False
        else:
            print("ungültige eingabe")
    spalte = action
    return spalte

def rendern(feld):
    #aktuelles feld rendern
    for i in range(6):
        print(feld[i])
    print("_____________________")
    print (list(range(7)))

def steinsetzen(spielfeld, spalte, spieler):
    #ersten freien Platz suchen
    #stein für aktuellen spieler abspeichern
    for zeile in range(5,-1,-1):
        if spielfeld[zeile][spalte] == 0:
            spielfeld[zeile][spalte] = spieler
            break
    return spielfeld

def errortest(spielfeld, spalte):
    #testen ob oberstes Element der Spalte leer ist
    if spielfeld[0][spalte] != 0:
        error = True
        print("Spalte bereits voll")
    else:
        error = False
    return error




def spiel():
    spiel = True
    win = False
    spielfeld = initialisieren()
    rendern(spielfeld)
    while spiel:
        error = True
        while error == True:
            spalte = action()
            error = errortest(spielfeld, spalte)
        spielfeld = steinsetzen(spielfeld, spalte, 1)
        rendern(spielfeld)
        win = wincheck(spielfeld, 1)
        if win == True:
            spiel = False
            winner = 1
            break
        error = True
        while error == True:
            spalte = action()
            error = errortest(spielfeld, spalte)
        spielfeld = steinsetzen(spielfeld, spalte, 2)
        rendern(spielfeld)
        win = wincheck(spielfeld, 2)
        if win == True:
            spiel = False
            winner = 2
            break
    #Winnerscreen mit winner
    print("gewinner ist spieler", winner)



spiel()
