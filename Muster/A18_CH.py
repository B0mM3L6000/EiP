#Aufgabenteile 1,2 und 3 in einem

import random
# Erzeugung eines Labyrinthes aus m Zeilen und n Spalten
# Zum Verständnis der Wegesuche ist es nicht wichtig, auf welche
# Art und Weise das Labyrinth, in dem ein Weg gesucht werden soll,
# entstanden ist.
def generiere_labyrinth(m, n):
    lab = [['#' for x in range(n)] for y in range(m)]
    besucht = [[False for x in range(n)] for y in range(m)]

    for y in range(1, m - 1, 2):
        for x in range(1, n - 1, 2):
            lab[y][x] = ' '

    # Der Algorithmus zur Erzeugung des Labyrinthes basiert auf
    # einer randomisierten Tiefensuche.
    lifo = []
    (y, x) = (m // 2, n // 2)
    lifo.append((y, x))
    besucht[y][x] = True

    while len(lifo) > 0:
        (y, x) = lifo.pop()

        r = [0, 1, 2, 3]
        for i in range(3):
            j = random.randint(i, 3)
            r[i], r[j] = r[j], r[i]

        for i in range(4):
            if r[i] == 0:
                if x > 2 and not besucht[y][x - 2]:
                    lifo.append((y, x - 2))
                    besucht[y][x - 2] = True
                    lab[y][x - 1] = ' '
            elif r[i] == 1:
                if x < n - 3 and not besucht[y][x + 2]:
                    lifo.append((y, x + 2))
                    besucht[y][x + 2] = True
                    lab[y][x + 1] = ' '
            elif r[i] == 2:
                if y > 2 and not besucht[y - 2][x]:
                    lifo.append((y - 2, x))
                    besucht[y - 2][x] = True
                    lab[y - 1][x] = ' '
            elif r[i] == 3:
                if y < m - 3 and not besucht[y + 2][x]:
                    lifo.append((y + 2, x))
                    besucht[y + 2][x] = True
                    lab[y + 1][x] = ' '

    lab[0][n // 2] = ' '
    lab[m - 1][n // 2] = ' '

    return lab

# Suche eines Weges im Labyrinth lab vom Startpunkt start zu
# allen erreichbaren Feldern des Labyrinthes
def breitensuche(lab, start):
    m = len(lab) # Zahl der Zeilen
    n = len(lab[0]) # Zahl der Spalten
    # Das zweidimensionale vorgaenger-Feld dient zur Speicherung der
    # Koordinaten des Feldes, von wo aus das betrachtete Feld (x,y) bei
    # der Wegesuche besucht wurde.
    vorgaenger = [[(0, 0) for x in range(n)] for y in range(m)]
    # Das zweidimensionale besucht-Feld dient zur Markierung bereits
    # besuchter Felder, die sich schon in dem FIFO-Speicher befinden.
    besucht = [[False for x in range(n)] for y in range(m)]

    fifo = []
    (y, x) = start
    fifo.append((y, x))
    # markiere das start-Feld als besucht.
    besucht[y][x] = True

    while len(fifo) > 0:
        (y, x) = fifo.pop(0)
        # markiere dieses erreichte Feld, um bei der späteren Ausgabe
        # sehen zu können, welche Felder überhaupt erreichbar waren.
        lab[y][x] = '.'

        if x > 0 and lab[y][x - 1] == ' ' and not besucht[y][x - 1]:
            vorgaenger[y][x - 1] = (y, x)
            fifo.append((y, x - 1))
            besucht[y][x - 1] = True
        if x < n - 1 and lab[y][x + 1] == ' ' and not besucht[y][x + 1]:
            vorgaenger[y][x + 1] = (y, x)
            fifo.append((y, x + 1))
            besucht[y][x + 1] = True
        if y > 0 and lab[y - 1][x] == ' ' and not besucht[y - 1][x]:
            vorgaenger[y - 1][x] = (y, x)
            fifo.append((y - 1, x))
            besucht[y - 1][x] = True
        if y < m - 1 and lab[y + 1][x] == ' ' and not besucht[y + 1][x]:
            vorgaenger[y + 1][x] = (y, x)
            fifo.append((y + 1, x))
            besucht[y + 1][x] = True
    return vorgaenger

# Mit Hilfe dieser Funktion rekonstruieren wir im Labyrinth einen Weg vom ziel-Feld
# rückwärts zum start-Feld und "zeichnen" diesen Weg ein.
def markiere_gefundenen_weg(lab, wege, start, ziel):
    (y, x) = ziel
    d=0
    while wege[y][x] != (0, 0):
        lab[y][x] = 'o'
        (y, x) = wege[y][x]
        d+=1
    (y, x) = start
    lab[y][x] = 'o'
    return(d)

# Funktion zur Ausgabe unseres Labyrinthes
def print_labyrinth(lab):
    for y in range(0, len(lab)):
        for x in range(0, len(lab[y])):
            print(lab[y][x], end='')
        print()

# Hauptprogramm

# Festlegung der Labyrinthgröße
m = 19
n = 39

# Erzeugung eines zufälligen Labyrinthes
lab = generiere_labyrinth(m, n)
# print_labyrinth(lab)

# Festlegung von start- und ziel-Feldes
start = (0, n // 2)
ziel = (m - 1, n // 2)

# Durchführung der Tiefensuche
wege = breitensuche(lab, start)

# Überprüfung, ob ein Weg gefunden werden konnte
(y, x) = ziel
if wege[y][x] == (0, 0):
    print('Kein Weg gefunden')

# Markierung des gefundenen Weges
markiere_gefundenen_weg(lab, wege, start, ziel)

lab[0][n // 2] = 'S'
lab[m - 1][n // 2] = 'Z'

# Ausgabe des Labyrinthes, der erreichbaren Felder
# und des gefundenen Weges
print_labyrinth(lab)
print(markiere_gefundenen_weg(lab, wege, start, ziel))