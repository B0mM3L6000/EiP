import random

# Aufgabe 12_2

# Lottozahlen ziehen
pool = []                   # Erzeuge leere Liste für den Pool aus Lottozahlen
lottozahlen = []            # Erzeuge leere Liste für die gezogenen Zahlen


for i in range(1,50):       # Fülle den Pool mit ganzen Zahlen
    pool.append(i)

for i in range(1, 7):                           # Ziehe 6 Mal
    x = random.randint(0, len(pool)-1)       # Wähle ein zufälliges Element aus der Liste
    lottozahlen.append(pool[x])                    # Füge das Element dem Pool der gezogenen Lottozahlen hinzu
    pool.remove(pool[x])                           # Lösche das Element aus dem Pool

lottozahlen.sort()          # Aufsteigende Sortierung der Feldelemente
print('Die Lottozahlen von heute: ', lottozahlen)          # Lottozahlen ausgeben


# Aufgabe 12_3

tip = []

# Eingabe eigener Lottzahlen und verpacken in eine Liste
for i in range(1,7):       # Fülle den Pool mit ganzen Zahlen
    a = int(input('Tippen Sie eine Lottozahl ein: ' ))
    if a < 1 or a > 49 or a in tip:            # Prüfe, ob Zahl zwischen 1 und 49 und noch nicht getippt
        print('Diese Zahl ist nicht gültig.')
        a = int(input('Tippen Sie eine neue Lottozahl zwischen 1 und 49 ein: '))
    tip.append(a)

# Lottozahlen ziehen
pool = []                   # Erzeuge leere Liste für den Pool aus Lottozahlen
lottozahlen = []            # Erzeuge leere Liste für die gezogenen Zahlen

for i in range(1,50):       # Fülle den Pool mit ganzen Zahlen
    pool.append(i)

for i in range(0, 6):                           # Ziehe 6 Mal
    x = random.randint(0, len(pool)-1)       # Wähle ein zufälliges Element aus der Liste
    lottozahlen.append(pool[x])                    # Füge das Element dem Pool der gezogenen Lottozahlen hinzu
    pool.remove(pool[x])                           # Lösche das Element aus dem Pool


# Prüfen, ob man gewonnen hat
# Abfrage, ob der Wert x im Feld a abgelegt ist.
richtige = 0
for i in range(0, 6):
    if tip[i] in lottozahlen:
        print(tip[i], ' wurde richtig getippt!')
        richtige += 1
    else:
        print(tip[i], ' wurde falsch getippt!')

lottozahlen.sort()
print('Die Lottozahlen lauten:', lottozahlen)
print('Sie haben ', richtige, 'Richtige von 6.')