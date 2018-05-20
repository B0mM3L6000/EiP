import pygame as pg

"""

Höhe mal Breite: 6x7
4 gleiche Steine aneinander diagonalrunter/diagonalhoch/horizontal/vertikal gewinnt
beide Spieler ziehen nacheinander
wählen eine spalte und der stein wird dann auf den untersten freien spaltenplatz gesetzt
nach jedem stein überprüfen, ob ein spieler gewonnen hat

"""

def initialisieren():
    #leeres 6x7 feld erstellen


def wincheck(spieler):
    #feld aufrufen
    #gewonnen = False
    #checken für jede zeile
        #ob 4 in einer reihe nacheinander gleich sind
        #if ja
            #aktueller spieler gewinnt
            #gewonnen = True
    #checken für jede spalte
        #ob 4 in einer reihe nacheinander gleich sind
        #if ja
            #aktueller spieler gewinnt
            #gewonnen = True
    #checken für jede diagonalerunter
        #ob 4 in einer reihe nacheinander gleich sind
        #if ja
            #aktueller spieler gewinnt
            #gewonnen = True
    #checken für jede diagonalhoch
        #ob 4 in einer reihe nacheinander gleich sind
        #if ja
            #aktueller spieler gewinnt
            #gewonnen = True
    #return gewonnen

def action(spieler):
    #aktion für aktuellen spieler ermöglichen + rendern
    #return ausgewählte spalte

def rendern(feld):
    #aktuelles feld rendern

def steinsetzen(spalte, spieler):
    #überprüfen ob spalte voll ist:
        #return error
        #break
    #ansonsten
        #ersten freien Platz suchen
        #stein für aktuellen spieler abspeichern
        #return neues feld




def spiel():
    #leeres feld initialisieren
    #rendern
    #solange spiel noch nicht gewonnen ist:
        #spieler rot setzt Stein:
        #action auswählen
        #steinsetzen
        #rendern
        #check ob gewonnen ist
        #if ja -> break und spielende mit gratz an rot
        #spieler gelb setzt stein
        #action auswählen
        #steinsetzen
        #rendern
        #check ob gewonnen ist
        #if ja -> break und spielende mit gratz an gelb



spiel()
