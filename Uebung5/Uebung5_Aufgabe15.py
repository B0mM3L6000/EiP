import pygame as pg
import time

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


def action(spielfeld, bildschirm, spieler):
    #aktion für aktuellen spieler ermöglichen + rendern
    action = 3
    if spieler == 1:
        tmpspieler = 1
    elif spieler == 2:
        tmpspieler = 2
    inputende = False
    while not inputende:
        for e in pg.event.get():
            if e.type == pg.KEYDOWN:
                # Wenn die Pfeil-nach-links-Taste gedrückt wurde, bewegen wir den Kreis nach links.
                if e.key == pg.K_LEFT:
                    if action -1 < 0:
                        action = 0
                    else:
                        action -= 1
                    rendern(spielfeld, bildschirm, tmpspieler, action)
                # Wenn die Pfeil-nach-rechts-Taste gedrückt wurde, bewegen wir den Kreis nach rechts.
                elif e.key == pg.K_RIGHT:
                    if action +1 > 6:
                        action = 6
                    else:
                        action += 1
                    rendern(spielfeld, bildschirm, tmpspieler, action)
                elif e.key == pg.K_RETURN:
                    inputende = True
    """
    fehler = True
    while fehler == True:
        #action = int(input("Welche Spalte (0-6)?"))
        if action >=1 and action <=7:
            fehler = False
        else:
            print("ungültige eingabe")
    """
    spalte = action
    return spalte

def rendern(feld, bildschirm, spieler, action):
    #aktuelles feld rendern
    """
    for i in range(6):
        print(feld[i])
    print("_____________________")
    print (list(range(1,8)))
    """
    zeilen = 7
    spalten = 7
    zellbreite = 100
    weiss = [255,255,255]
    gelb = [0,255,0]
    rot = [255,0,0]
    blau = [0,0,255]
    bildschirm.fill(blau)
    pg.draw.rect(bildschirm,weiss,(0,0,700,100))
    for zeile in range(1,zeilen):
        for spalte in range(spalten):
            if feld[zeile-1][spalte] == 0:
                pg.draw.circle(bildschirm, weiss,(spalte*100+50,zeile*100+50),45)
            elif feld[zeile-1][spalte] == 1:
                pg.draw.circle(bildschirm, gelb,(spalte*100+50,zeile*100+50),45)
            elif feld[zeile-1][spalte] == 2:
                pg.draw.circle(bildschirm, rot,(spalte*100+50,zeile*100+50),45)
    if spieler == 1:
        pg.draw.circle(bildschirm, gelb, (action*100+50,50),45)
    elif spieler == 2:
        pg.draw.circle(bildschirm, rot, (action*100+50,50), 45)
    pg.display.flip()

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
        #print("Spalte bereits voll")
    else:
        error = False
    return error

def pygamestart(spielfeld):
    zeilen = 7
    spalten = 7
    zellbreite = 100
    weiss = [255,255,255]
    geld = [0,255,0]
    rot = [255,0,0]
    blau = [0,0,255]
    pg.init()
    pg.display.set_caption("Vier gewinnt")
    bildschirm = pg.display.set_mode((spalten*zellbreite,zeilen*zellbreite))
    #clock = pg.time.Clock()
    bildschirm.fill(blau)
    pg.draw.rect(bildschirm,weiss,(0,0,700,100))
    for zeile in range(1,zeilen):
        for spalte in range(spalten):
            if spielfeld[zeile-1][spalte] == 0:
                pg.draw.circle(bildschirm, weiss,(spalte*100+50,zeile*100+50),45)
            elif spielfeld[zeile-1][spalte] == 1:
                pg.draw.circle(bildschirm, gelb,(spalte*100+50,zeile*100+50),45)
            elif spielfeld[zeile-1][spalte] == 2:
                pg.draw.circle(bildschirm, rot,(spalte*100+50,zeile*100+50),45)
    pg.display.flip()
    return bildschirm


def spiel():
    spiel = True
    win = False
    spielfeld = initialisieren()
    bildschirm = pygamestart(spielfeld)
    rendern(spielfeld, bildschirm, 1, 3)
    while spiel:
        error = True
        while error == True:
            spalte = action(spielfeld, bildschirm, 1)
            error = errortest(spielfeld, spalte)
        spielfeld = steinsetzen(spielfeld, spalte, 1)
        rendern(spielfeld, bildschirm,2, 3)
        win = wincheck(spielfeld, 1)
        if win == True:
            spiel = False
            winner = 1
            break
        error = True
        while error == True:
            spalte = action(spielfeld, bildschirm, 2)
            error = errortest(spielfeld, spalte)
        spielfeld = steinsetzen(spielfeld, spalte, 2)
        rendern(spielfeld, bildschirm,1, 3)
        win = wincheck(spielfeld, 2)
        if win == True:
            spiel = False
            winner = 2
            break
    #Winnerscreen mit winner
    font = pg.font.SysFont('Times', 100, False, False)
    schwarz = [0,0,0]
    gruen = [0,255,0]
    rot = [255,0,0]
    if winner == 1:
        bildschirm.fill(gruen)
    elif winner == 2:
        bildschirm.fill(rot)
    text = font.render('Gewonnen!',True,schwarz)
    bildschirm.blit(text,[135,250])
    pg.display.flip()
    time.sleep(2)
    #print("gewinner ist spieler", winner)



spiel()
