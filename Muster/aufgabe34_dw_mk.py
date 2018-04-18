#Aufgabe34.1-----------------------------------------------------------------------
datei = open('Maennernamen.txt', 'r', encoding='ISO-8859-1')

#Füge alle Namen in ein Feld
namen =[]
for line in datei:
    namen.append(line)
print("Anzahl der Männernamen:",len(namen))
#Nun wird überprüft, ob Namen doppelt vorkommen
entferne = []
for i in range (0,len(namen)):
    for j in range (0,len(namen)):
        if i == j:
            continue
        #Ist dies der Fall, so merke ich mir die Stelle der zu enfernenden Namen im Feld "entferne"
        if namen[i] == namen[j] and i < j and j not in entferne:
            entferne.append(j)

#nun müssen die jeweiligen Stellen auch entfernt werden
#allerdings müssen die Namen in "namen" von hinten entfernt
#werden, da es sonst zu Indexverschiebungen käme
#und gegebenenfalls die falschen Namen entfernt werden würden
entferne.sort()
for i in reversed(entferne):
    namen.pop(i)
print("Anzahl der Männernamen nach Eliminierung:", len(namen))
datei.close()

datei = open('Frauennamen.txt', 'r', encoding='ISO-8859-1')
namen =[]
for line in datei:
    namen.append(line)
print("Anzahl der Frauennamen:",len(namen))
entferne = []
for i in range (0,len(namen)):
    for j in range (0,len(namen)):
        if i == j:
            continue
        if namen[i] == namen[j] and i < j and j not in entferne:
            entferne.append(j)
entferne.sort()
for i in reversed(entferne):
    namen.pop(i)
print("Anzahl der Frauennamen nach Eliminierung:", len(namen))
datei.close()

#Aufgabe34.2-----------------------------------------------------------------------
datei = open('Maennernamen.txt', 'r', encoding='ISO-8859-1')

#Namen werden in ein Feld eingefügt und anschließend sortiert
namen =[]
for line in datei:
    namen.append(line)
namen.sort()

#Ein Name wird immer mit dem Nächsten verglichen
#die Stelle der doppelten Namen wird gemerkt
entferne = []
for i in range(0,len(namen)-1):
    if namen[i] == namen[i+1]:
        entferne.append(i+1)
#Entfernen der gemerkten Stellen
for i in reversed(entferne):
    namen.pop(i)
print("Anzahl der Männernamen nach Eliminierung mit einer sortierten Liste:", len(namen))
datei.close()

datei = open('Frauennamen.txt', 'r', encoding='ISO-8859-1')
namen =[]
for line in datei:
    namen.append(line)
namen.sort()
entferne = []
for i in range(0,len(namen)-1):
    if namen[i] == namen[i+1]:
        entferne.append(i+1)
for i in reversed(entferne):
    namen.pop(i)
print("Anzahl der Frauennamen nach Eliminierung mit einer sortierten Liste:", len(namen))
datei.close()

#Aufgabe34.3-----------------------------------------------------------------------
datei = open('Maennernamen.txt', 'r', encoding='ISO-8859-1')
#Füge alle Namen in ein Feld
namen =[]
for line in datei:
    namen.append(line)
namen = set(namen)
print("Anzahl der Männernamen nach Eliminierung mit einem Set:", len(namen))
datei.close()

datei = open('Frauennamen.txt', 'r', encoding='ISO-8859-1')
namen =[]
for line in datei:
    namen.append(line)
namen = set(namen)
print("Anzahl der Frauennamen nach Eliminierung mit einem Set:", len(namen))
datei.close()

#Aufgabe34.4-----------------------------------------------------------------------
datei1 = open('Maennernamen.txt', 'r', encoding='ISO-8859-1')
datei2 = open('Frauennamen.txt', 'r', encoding='ISO-8859-1')
datei3 = open('all_names.txt','w')

alles = []
maenner =[]
frauen = []
for line in datei1:
    maenner.append(line)
for line in datei2:
    frauen.append(line)
maenner = set(maenner)
frauen = set(frauen)

for i in maenner:
    if i in frauen:
        alles.append(i)
print("Anzahl der gemeinsamen Namen:",len(alles))
alles = str(alles)
datei3.write(alles)

datei1.close()
datei2.close()
datei3.close()