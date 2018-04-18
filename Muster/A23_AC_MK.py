# Ein einfaches 7x7 Hidoku
feld1 =[[ 2, 0, 0, 0,11,38, 0],
        [ 0, 1, 8, 0, 0,41,40],
        [ 5, 0, 0, 0, 0, 0,49],
        [ 0, 0, 0, 0, 0,47, 0],
        [ 0,20, 0,33, 0, 0,45],
        [16, 0,23,26, 0,31, 0],
        [ 0,18,24, 0, 0, 0,29]]

# Ein schwierigeres 8x8 Hidoku
feld2 =[[ 0, 0, 0, 0,38, 0,35,34],
        [ 3, 1, 0, 0, 0, 0, 0, 0],
        [ 0, 8, 0,60,53, 0, 0, 0],
        [ 0, 0, 0,63,59, 0,41, 0],
        [ 0,47,64, 0, 0,55, 0, 0],
        [ 0,18, 0, 0, 0, 0, 0,26],
        [13, 0, 0, 0, 0,28, 0, 0],
        [ 0, 0, 0, 0,21, 0, 0, 0]]

feld3 =[[ 0, 0, 0,15,16,17, 0, 7, 6],
        [78, 0,81, 0, 0, 0,18, 0, 5],
        [76, 0, 0,66,67, 0,19, 3, 0],
        [ 0, 0,64,68, 0, 0,29,30, 0],
        [ 0,73,70, 0, 0, 0, 0,32, 1],
        [ 0,72, 0, 0, 0, 0,26,35, 0],
        [ 0, 0, 0, 0,47, 0, 0,37, 0],
        [59, 0,51,52, 0, 0, 0, 0, 0],
        [58, 0, 0,49, 0, 0, 0,42,41]]

feld4 =[[ 0, 0,93, 0, 0, 0,  0, 0, 0,57],
        [ 0, 0, 0,22, 0,53, 54,40, 0, 0],
        [ 0, 0,18,23,52, 0,100, 0, 0, 0],
        [ 0, 0, 0, 0, 0,99, 33, 0, 0, 0],
        [ 0, 0, 0, 0, 0,25,  0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0,  0, 0, 0,29],
        [14, 0, 7, 0, 0, 0,  0, 0, 0, 0],
        [ 0, 0, 0,65, 0, 0, 46,72,77, 0],
        [ 0, 9, 0, 0, 0, 0,  0, 0,80,76],
        [ 1, 0, 0,11, 0,68, 82, 0, 0, 0]]

# Die Ausgabe findet statt, wenn das Feld gelöst wurde
def print_hidoku(feld):
    n = len(feld)
    for i in range(n):
        for j in range(n):
            print('{0:4d}'.format(feld[i][j]), end='')
        print()
    print()

# Das ganze Feld wird durchgegangen, bis die Startnummer 1 gefunden wird. Die Koordinaten werden dann zurückgegeben
def find_start(feld):
    n = len(feld)
    for i in range(n):
        for j in range(n):
            if feld[i][j] == 1:
                return (i,j)

# In dem Feld fixed ist die Position i = True, falls i als feste Nummer im Feld vorgegeben ist
def set_fixed(feld):
    n = len(feld)
    fixed = [False for i in range(n*n+1)]
    for i in range(n):
        for j in range(n):
            fixed[feld[i][j]] = True
    return fixed

# Das ist die Hauptfunktion, die das Feld mit den Nummern besetzt
def solve_hidoku(feld,z,s):
    # Die Zugnummer wird zugewiesen
    number = feld[z][s]
    n = len(feld)
    # Falls die letzte gesetzte Nummer schon die letzte Nummer ist, ist die Funktion am Rekursionsanfang
    # Wenn nicht, läuft die Funktion weiter und versucht die nächste Nummer zu setzten
    if number == n*n:
        return True
    # Der nächste Zug ist number+1
    number += 1
    # Es wird für alle erreichbaren Felder geschaut, ob die zu setztende Nummer darin vorkommt.
    # Ist die Zeile oder Spalte <0 oder >= n, ist dies nicht mehr im Feld
    # Wenn ja, dann gilt dieser Zug als ausgeführt und die Funktion ruft sich mit mit den Koordinaten dieser Nummer´auf
    for i in range(-1,2):
        if z+i < 0 or z+i >= n:
            continue
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if s+j < 0 or s+j >= n:
                continue
            if feld[z+i][s+j] == number:
                return solve_hidoku(feld,z+i,s+j)

    # Falls die Nummer, die jetzt gesetzt werden soll, schon (unerreichbar) irgendwo im Feld steht, dann ist ein Fehler passiert
    # Es wird False zurückgegeben und die aeussere Funktion muss dann die gesetzte Nummer an eine andere Position setzen
    if fixed[number]:
        return False

    # Hier wird die Nummer an die erreichbare Position (z+i, s+i) gesetzt. Danach ruft die Funktion sich rekursiv auf und
    # versucht, auch die folgenden Nummern auf diese Weise zu setzten. Wenn alle weiteren Aufrufe True zurückgebene, ist
    # das Feld fertig besetzt. Wenn nicht, dann wird dieses Feld mit 0 belegt, nicht mehr in diesem Durchlauf beachtet
    # und eine andere Position besetzt. Wenn die Schleife komplett durchgelaufen ist, dann muss der Zug von der Funktion
    # darüber falsch gewesen sein.

    for i in range(-1,2):
        if z+i < 0 or z+i >= n:
            continue
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if s+j < 0 or s+j >= n:
                continue
            if feld[z+i][s+j] > 0:
                continue
            feld[z+i][s+j] = number
            if solve_hidoku(feld,z+i,s+j):
                return True
            feld[z+i][s+j] = 0

    return False

# In dem Feld fixed werden alle Nummern gespeichert, die schon fest stehen
fixed = set_fixed(feld1)
# Hier werden die Startkoordinaten gesucht
(start_x,start_y) = find_start(feld1)
# Falls es eine Lösung gibt, wird diese ausgegeben
if solve_hidoku(feld1,start_x,start_y):
    print_hidoku(feld1)