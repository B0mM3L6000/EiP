"""Aus 15. 1 Kopiert:"""
import random

# Größe des Spielfeldes
n = 10
# Spielfeld
feld = [[-1 for x in range(n)] for y in range(n)]
# Schiffslängen
sl = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]
# maximale Anzahl von Platzierungsversuchen für ein Schiff
anzahl_platzierungsversuche = 10

overlap = True

while overlap:
    # Wir entfernen alle bisher gesetzten Schiffe.
    for y in range(0, n):
        for x in range(0, n):
            feld[y][x] = -1 # leeres Feld

    overlap = False

    for i in range(0, len(sl)):
        for k in range(0, anzahl_platzierungsversuche):
            # Wähle zufällige Orientierung des i-ten Schiffes
            orientation = random.randint(0, 1)

            # (x0,y0) ist die linke obere Ecke des zu platzierenden Schiffes
            # Alle Felder, die das Schiff belegt und alle Felder, die das Schiff berühren
            # sind gegeben durch [x1,x2] x [y1,y2].
            if orientation == 0: # horizontal
                x0 = random.randint(0, n - sl[i])
                y0 = random.randint(0, n - 1)
                x2 = min(n - 1, x0 + sl[i] + 1)
                y2 = min(n - 1, y0 + 1)
            else: # vertikal
                x0 = random.randint(0, n - 1)
                y0 = random.randint(0, n - sl[i])
                x2 = min(n - 1, x0 + 1)
                y2 = min(n - 1, y0 + sl[i] + 1)

            x1 = max(0, x0 - 1)
            y1 = max(0, y0 - 1)

            # Nachbarschaft [x1,x2] x [y1,y2] des Schiffes muss frei sein!

            overlap_i = False
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    if feld[y][x] >= 0:
                        overlap_i = True
                        break
                if overlap_i:
                    break

            if overlap_i: # Der aktuelle Platzierungsversuch für das i-te Schiff ist gescheitert.
                # Wir versuchen das i-te Schiff erneut zu platzieren.
                continue

            # Wir haben Freiraum für das i-te Schiff und seine unmittelbare Umgebung gefunden.
            if orientation == 0:
                # Wir platzieren das i-te Schiff horizontal mit der linken oberen Ecke (x0,y0)
                for x in range(x0, x0 + sl[i]):
                    if feld[y0][x] < 0:
                        feld[y0][x] = i
            else:
                # Wir platzieren das i-te Schiff vertikal mit der linken oberen Ecke (x0,y0)
                for y in range(y0, y0 + sl[i]):
                    if feld[y][x0] < 0:
                        feld[y][x0] = i
            # Für das i-te Schiff benötigen wir keine weiteren Platzierungsversuche.
            break
        else: # Alle Platzierungsversuche sind gescheitert, das i-te Schiff zu platzieren.
            # Wir beginnen ganz von vorne.
            overlap = True
            break

"""Spielfeldzeichnung, damit man nicht blind spielt, leicht abgewandelt zu 15.1:"""
kopf = '    1 2 3 4 5 6 7 8 9 10'
zeile = 'ABCDEFGHIJ'

print(kopf)
print()
for y in range(0, n):
    print(zeile[y], end='   ')
    for x in range(0, n):
        if feld[y][x] < 0:
            print('.', end=' ')
        else:
            print(feld[y][x], end=' ')
    print()
print("\n")

'''
###################################################################################################################
Meine Erweiterung
###################################################################################################################
'''

nochnicht_zuende = True
# um eine Referenz zu haben, wieviele verschiedene Schiffe es gibt:
vergleichswert = len(sl)

while nochnicht_zuende: #Diese loop wird verlassen, wenn fieldsum == 0 am Ende der Iterantion ist.

    #Zeichne verdecktes Spielfeld, -1 bis 9: '.' -2: 'x'
    print(kopf)
    print()
    for y in range(0, n):
        print(zeile[y], end='   ')
        for x in range(0, n):
            if feld[y][x] >= -1:
                print('.', end=' ')
            else:
                print('x', end=' ')
        print()
    print()

    eingabe = True
    while eingabe: #Zum Abfangen von falschen integer-Werten, könnte noch verbessert werden, damit Strings abgefangen werden können
        x_eingabe = int(input("Gebe eine x-Koordinate (1-10) ein: "))
        y_eingabe = int(input("Gebe eine y-Koordinate (1-10) ein: "))
        print()

        if x_eingabe >=1 and x_eingabe <=10 and y_eingabe >=1 and y_eingabe <=10:
            x_schuss = x_eingabe -1
            y_schuss = y_eingabe -1
            if feld[y_schuss][x_schuss] >= 0:
                print(">>>>>>>>>> Treffer!!! <<<<<<<<<<")
            else:
                print(">>>>> Daneben... <<<<<")
            feld[y_schuss][x_schuss] = -2
            eingabe = False
        else:
            print("Das ist keine gueltige Koordinate.")
        print()


    schiffe = [] #Menge der mit Schiffen belegten Koordinaten, flacher leerer Array.
    fieldsum = 0 #fieldsum = 0 zuordnen.

    for y in range(0, n):
        for x in range(0, n): #Alle Koordniaten in 2D absuchen
            if feld[y][x] >= 0: #bei 0,1,2,...,9
                schiffe.append(feld[y][x]) #eine Koordinate zu Schiffen flach hinzufügen
                fieldsum += 1 #fieldsum +1


    if fieldsum > 0: #Wenn es noch Koordinaten gibt, die mit Schiffen belegt sind.

        #Wie Aufgabe 14.3:
        schiffe.sort()
        v = 0
        for s in range(len(schiffe)):
            if schiffe[s] != schiffe[s - 1]:
                v += 1

        if v != vergleichswert: #Dies tritt nur ein, wenn direkt zuvor alle Elemente einer bestimmten Größe aus dem Schiffe-Array entfernt wurden.
            print(">>>>>>>>>>>>>>>>>>>> Versenkt!!!!!! <<<<<<<<<<<<<<<<<<<<\n")

        vergleichswert = v #vergleichswert an verschiedene Einträge v in Schiffe-Array anpassen.

    else: #Wenn es keine Koordinaten gibt, die mit Schiffen belegt sind.
        nochnicht_zuende = False #Ende der while-Loop in Zeile 104.
        print("########## Spielende: Du hast alle Schiffe versenkt! ##########") #Endausgabe.