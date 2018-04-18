#Aufgabenteil 1
b = []

Spalten = int(input("Geben Sie die Anzahl der Reihen des auszugebenen Pascallschen Dreiecks, an: "))

for i in range (0, Spalten):
    b.append([])
    for j in range (0, i+1):
        if j == 0 or j == i:
            b[i].append(1)
        else:
            b[i].append(b[i-1][j-1]+b[i-1][j])

for i in range(0, len(b)):
    for j in range (0, len(b[i])):
        print(b[i][j], end =' ')
    print()


#Aufgabenteil 2
#Zeile: 1 Felder: 1
#Zeile: 2 Felder: 2 + 1
#Zeile: 3 Felder: 3 + 3
#Zeile: 4 Felder: 4 + 4 + 2
#Zeile: 5 Felder: 5 + 5 + 5
#Zeile: 6 Felder: 6 + 6 + 6 + 3
#Zeile: 7 Felder: 7 + 7 + 7 + 7
#Zeile: 8 Felder: 8 + 8 + 8 + 8 + 4

#Bei ungerader Zeilen Anzahl: Felder = ((n+1)/2)*n -> (n+1) * n / 2 -> ((n^2) + n) / 2
#Bei gerader Zeilen Anzahl: Felder = (n/2) * n + (n/2) -> ((n^2) / 2) + (n/2) -> ((n^2) + n) / 2

b = []
c = []

zeilen = int(input('Geben Sie die Anzahl der zu speichernden Zeilen an: '))

for i in range (0, zeilen):
    b.append([])
    for j in range (0, i+1):
        if j == 0 or j == i:
            b[i].append(1)
        else:
            b[i].append(b[i-1][j-1]+b[i-1][j])

for i in range (0, zeilen):
    for j in range (0, i+1):
        c.append(b[i][j])

speichern = ((zeilen ** 2)+ zeilen)//2

print(speichern)
print(len(c))