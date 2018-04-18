import random


# Funktionen, um den Code zu verschlanken
def pruefe_siegbedingung(getroffenes_schiff, person):
    """ Funktion prüft, ob alle schiffe_spieler versenkt wurden"""
    if person == "Spieler":
        if schiffe_spieler[getroffenes_schiff] == 0:
            print("Schiff versenkt!")
            if schiffe_spieler.count(0) == len(schiffe_spieler):
                return True
                print("Du hast gewonnen!")
    else:
        if schiffe_gegner.count(0) == len(schiffe_gegner):
            return True
            print("Computer hat gewonnen!")
    return False


def generierefeld_spieler():
    """generiert ein neues Spielfeld_spieler"""
    feld_spieler = [[-1 for x in range(n)] for y in range(n)]
    overlap = True

    while overlap:
        # Wir entfernen alle bisher gesetzten schiffe_spieler.
        for y in range(0, n):
            for x in range(0, n):
                feld_spieler[y][x] = -1  # leeres feld_spieler

        overlap = False

        for i in range(0, len(sl)):
            for k in range(0, anzahl_platzierungsversuche):
                # Wähle zufällige Orientierung des i-ten schiffe_spielers
                orientation = random.randint(0, 1)

                # (x0,y0) ist die linke obere Ecke des zu platzierenden schiffe_spielers
                # Alle feld_spielerer, die das Schiff belegt und alle feld_spielerer, die das Schiff berühren
                # sind gegeben durch [x1,x2] x [y1,y2].
                if orientation == 0:  # horizontal
                    x0 = random.randint(0, n - sl[i])
                    y0 = random.randint(0, n - 1)
                    x2 = min(n - 1, x0 + sl[i] + 1)
                    y2 = min(n - 1, y0 + 1)
                else:  # vertikal
                    x0 = random.randint(0, n - 1)
                    y0 = random.randint(0, n - sl[i])
                    x2 = min(n - 1, x0 + 1)
                    y2 = min(n - 1, y0 + sl[i] + 1)

                x1 = max(0, x0 - 1)
                y1 = max(0, y0 - 1)

                # Nachbarschaft [x1,x2] x [y1,y2] des schiffe_spielers muss frei sein!

                overlap_i = False
                for y in range(y1, y2 + 1):
                    for x in range(x1, x2 + 1):
                        if feld_spieler[y][x] >= 0:
                            overlap_i = True
                            break
                    if overlap_i:
                        break

                if overlap_i:  # Der aktuelle Platzierungsversuch für das i-te Schiff ist gescheitert.
                    # Wir versuchen das i-te Schiff erneut zu platzieren.
                    continue

                # Wir haben Freiraum für das i-te Schiff und seine unmittelbare Umgebung gefunden.
                if orientation == 0:
                    # Wir platzieren das i-te Schiff horizontal mit der linken oberen Ecke (x0,y0)
                    for x in range(x0, x0 + sl[i]):
                        if feld_spieler[y0][x] < 0:
                            feld_spieler[y0][x] = i
                else:
                    # Wir platzieren das i-te Schiff vertikal mit der linken oberen Ecke (x0,y0)
                    for y in range(y0, y0 + sl[i]):
                        if feld_spieler[y][x0] < 0:
                            feld_spieler[y][x0] = i
                # Für das i-te Schiff benötigen wir keine weiteren Platzierungsversuche.
                break
            else:  # Alle Platzierungsversuche sind gescheitert, das i-te Schiff zu platzieren.
                # Wir beginnen ganz von vorne.
                overlap = True
                break
    return feld_spieler


def zeichne_spielfeld(person):
    # Ausgabe des aktualisierten Feldes
    if person == "Spieler":
        print()
        print("Dein Spielfeld:")
        print('    1 2 3 4 5 6 7 8 9 10')
        print()
        for y in range(0, n):
            print(zeile[y], end='   ')
            for x in range(0, n):
                if feld_spieler[y][x] >= -1:
                    print('.', end=' ')
                elif feld_spieler[y][x] == -2:
                    print("x", end=' ')
                else:
                    print("o", end=' ')
            print()
        print()
    else:
        print()
        print("Computers Spielfeld:")
        print('    1 2 3 4 5 6 7 8 9 10')
        print()
        for y in range(0, n):
            print(zeile[y], end='   ')
            for x in range(0, n):
                if feld_gegner[y][x] >= -1:
                    print('.', end=' ')
                elif feld_gegner[y][x] == -2:
                    print("x", end=' ')
                else:
                    print("o", end=' ')
            print()
        print()


def blockiere_benachbarte_felder(schiffsteile):
    for teil in schiffsteile:
        x = teil[0]
        y = teil[1]
        for horizontal in [-1, 0, 1]:
            for vertikal in [-1, 0, 1]:
                tmp_x = x + horizontal
                tmp_y = y + vertikal
                if -1 < tmp_x < n and -1 < tmp_y < n and erlaubter_schuss[tmp_y][tmp_x]:
                    erlaubter_schuss[tmp_y][tmp_x] = False
                    feld_gegner[tmp_y][tmp_x] = -3  # nur mal zum testen..


# Größe des Spielfeld_spieleres
n = 10
# Schiffslängen
sl = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]
# maximale Anzahl von Platzierungsversuchen für ein Schiff
anzahl_platzierungsversuche = 10

# Spielgenerierung
feld_gegner = generierefeld_spieler()
feld_spieler = generierefeld_spieler()

erlaubter_schuss = [[True for x in range(n)] for y in range(n)]

schiffe_spieler = sl[:]
schiffe_gegner = sl[:]

sieg = False
zug_spieler = True
teil_gefunden = False
letztes_x = -1
letztes_y = -1
suchrichtung = -1

tmp_schiff = []

zeile = 'ABCDEFGHIJ'

zeichne_spielfeld("Spieler")

while not sieg:
    # Code für den Zug des Spielers
    if zug_spieler:
        y = input("Zeile = ").upper()
        y = zeile.find(y)
        x = int(input("Spalte = "))
        x -= 1

        if feld_spieler[y][x] > -1:
            # Es wird ein Treffer gelandet - verringere Schiffsanzahl um eins, setze feld_spieler auf -2
            schiffe_spieler[feld_spieler[y][x]] -= 1
            print("Treffer")
            zug_spieler = True
            sieg = pruefe_siegbedingung(feld_spieler[y][x], "Spieler")
            feld_spieler[y][x] = -2
        elif feld_spieler[y][x] == -1:
            # Es wird Wasser getroffen - setze feld_spieler auf -3
            print("Wasser")
            feld_spieler[y][x] = -3
            zug_spieler = False
        else:
            # Wert auf feld_spieler ist < -1, somit wurde hier bereits einmal hingeschossen
            print("Da hast du schon mal hin geschossen.. Idiot ;-)")
            zug_spieler = False

        # Ausgabe des aktualisierten Feldes
        zeichne_spielfeld("Spieler")

    # Code für den Zug des Computers
    else:
        # im letzten Zug wurde kein Teil gefunden
        if not teil_gefunden:
            y = random.randint(0, 9)
            x = random.randint(0, 9)
            # Prüfe, ob der Schuss gültig ist (noch nicht dorthin geschossen, nicht durch Nebenbedingung ausgeschlossen.
            if erlaubter_schuss[y][x]:
                # im nächsten Zug darf hier nicht mehr hingeschossen werden
                erlaubter_schuss[y][x] = False

                # Es handelt sich um einen Treffer
                if feld_gegner[y][x] > -1:
                    schiffe_gegner[feld_gegner[y][x]] -= 1
                    print("Treffer")
                    teil_gefunden = True
                    tmp_schiff += [[x, y]]
                    letztes_x = x
                    letztes_y = y

                    # eigentlich kann dieser Fall gar nicht eintreten, da die Teile alle größer sind als 1
                    if schiffe_gegner[feld_gegner[y][x]] == 0:
                        print("Schiff versenkt!")
                        teil_gefunden = False
                        tmp_schiff = []
                        sieg = pruefe_siegbedingung(feld_gegner[y][x], "Computer")
                    feld_gegner[y][x] = -2

                # Es handelt sich um einen Wassertreffer. Nochmaliges Treffen auf ein Feld muss nicht berücksichtigt werden
                else:
                    print("Wasser")
                    feld_gegner[y][x] = -3
                    zug_spieler = True

        # es wurde bereits ein Teil gefunden
        else:
            # wir wissen noch nicht, wie rum das Schiff platziert ist
            if suchrichtung == -1:
                for horizontal in [-1, 0, 1]:
                    for vertikal in [-1, 0, 1]:
                        beende_schleife = False
                        # prüfe die benachbarten Felder
                        if (horizontal == 0 or vertikal == 0) and horizontal != vertikal:
                            tmp_y = letztes_y + vertikal
                            tmp_x = letztes_x + horizontal
                            # prüfe ob x und y auf dem Spielfeld und Schuss gültig ist
                            if -1 < tmp_y < n and -1 < tmp_x < n and erlaubter_schuss[tmp_y][tmp_x]:
                                erlaubter_schuss[tmp_y][tmp_x] = False

                                if feld_gegner[tmp_y][tmp_x] > -1:
                                    schiffe_gegner[feld_gegner[tmp_y][tmp_x]] -= 1
                                    print("Treffer")
                                    letztes_x = tmp_x
                                    letztes_y = tmp_y
                                    tmp_schiff += [[tmp_x, tmp_y]]

                                    # Bestimme die Orientierung des Schiffs
                                    if horizontal != 0:
                                        suchrichtung = 0
                                    else:
                                        suchrichtung = 1

                                    if schiffe_gegner[feld_gegner[tmp_y][tmp_x]] == 0:
                                        print("Schiff versenkt!")
                                        blockiere_benachbarte_felder(tmp_schiff)
                                        teil_gefunden = False
                                        suchrichtung = -1
                                        tmp_schiff = []
                                        sieg = pruefe_siegbedingung(feld_gegner[tmp_y][tmp_x], "Computer")
                                    feld_gegner[tmp_y][tmp_x] = -2
                                    beende_schleife = True
                                    break

                                else:
                                    print("Wasser")
                                    feld_gegner[tmp_y][tmp_x] = -3
                                    zug_spieler = True
                                    beende_schleife = True
                                    break
                    # wird benötigt, um doppelte Schleife zu beenden
                    if beende_schleife:
                        break

            # Schiff ist horizontal ausgerichtet
            elif suchrichtung == 0:

                # Durchlaufe das ganze Teilschiff, von hinten beginnend
                for coord in reversed(tmp_schiff):
                    letztes_x = coord[0]
                    letztes_y = coord[1]
                    # Prüfe die beiden Nachbarn
                    for horizontal in [-1, 1]:
                        beende_schleife = False

                        tmp_y = letztes_y
                        tmp_x = letztes_x + horizontal
                        if -1 < tmp_y < n and -1 < tmp_x < n and erlaubter_schuss[tmp_y][tmp_x]:
                            erlaubter_schuss[tmp_y][tmp_x] = False

                            if feld_gegner[tmp_y][tmp_x] > -1:
                                schiffe_gegner[feld_gegner[tmp_y][tmp_x]] -= 1
                                print("Treffer")
                                letztes_x = tmp_x
                                letztes_y = tmp_y
                                tmp_schiff += [[tmp_x, tmp_y]]

                                if schiffe_gegner[feld_gegner[tmp_y][tmp_x]] == 0:
                                    print("Schiff versenkt!")
                                    blockiere_benachbarte_felder(tmp_schiff)
                                    teil_gefunden = False
                                    suchrichtung = -1
                                    tmp_schiff = []
                                    sieg = pruefe_siegbedingung(feld_gegner[tmp_y][tmp_x], "Computer")
                                feld_gegner[tmp_y][tmp_x] = -2
                                beende_schleife = True
                                break
                            else:
                                print("Wasser")
                                feld_gegner[tmp_y][tmp_x] = -3
                                zug_spieler = True
                                beende_schleife = True
                                break
                    if beende_schleife:
                        break

            # Schiff ist vertikal ausgerichtet
            else:
                # Durchlaufe das ganze Teilschiff, von hinten beginnend
                for coord in reversed(tmp_schiff):
                    letztes_x = coord[0]
                    letztes_y = coord[1]
                    # Prüfe die beiden Nachbarn
                    for vertikal in [-1, 1]:
                        beende_schleife = False

                        tmp_y = letztes_y + vertikal
                        tmp_x = letztes_x
                        if -1 < tmp_y < n and -1 < tmp_x < n and erlaubter_schuss[tmp_y][tmp_x]:
                            erlaubter_schuss[tmp_y][tmp_x] = False

                            if feld_gegner[tmp_y][tmp_x] > -1:
                                schiffe_gegner[feld_gegner[tmp_y][tmp_x]] -= 1
                                print("Treffer")
                                letztes_x = tmp_x
                                letztes_y = tmp_y
                                tmp_schiff += [[tmp_x, tmp_y]]

                                if schiffe_gegner[feld_gegner[tmp_y][tmp_x]] == 0:
                                    print("Schiff versenkt!")
                                    blockiere_benachbarte_felder(tmp_schiff)
                                    teil_gefunden = False
                                    suchrichtung = -1
                                    tmp_schiff = []
                                    sieg = pruefe_siegbedingung(feld_gegner[tmp_y][tmp_x], "Computer")
                                feld_gegner[tmp_y][tmp_x] = -2
                                beende_schleife = True
                                break
                            else:
                                print("Wasser")
                                feld_gegner[tmp_y][tmp_x] = -3
                                zug_spieler = True
                                beende_schleife = True
                                break
                    if beende_schleife:
                        break

        zeichne_spielfeld("Computer")
