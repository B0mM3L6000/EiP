#Aufgabenteil 2
a = []
b = []
c = []

#Die Längen der Polynome wird eingelesen
laengeA = int(input("Geben Sie die Länge des ersten Polynoms an: "))
laengeB = int(input("Geben Sie die Länge des zweien Polynoms an: "))

#Die einzelnen Werte für a_0, a_1, ... , a_n werden Eingelesen
i = 0
while i != laengeA:
    print("An der Stelle x^",i," - ")
    a.append(int(input("Geben Sie den Wert des ersten Polynoms an: ")))
    #Kann man und wenn ja wie, eine Variable in den Input text Packen?
    i += 1

#Die einzelnen Werte für b_0, b_1, ..., b_n werden Eingelesen
i = 0
while i != laengeB:
    print("An der Stelle x^", i, " - ")
    b.append(int(input("Geben Sie den Wert des zweiten Polynoms an: ")))
    i += 1

#Es wird das längere Feld bestimmt und das kleinere mit Nullen aufgefüllt, so dass beide gleich lang sind
if len(a) != len(b):
    if len(a) > len(b):
        j = len(a) -len(b)
        for k in range (j, 0, -1):
            b.append(0)
    else:
        j = len(b) - len(a)
        for k in range (j, 0, -1):
            a.append(0)

#Das neue Polynom wird bestimmt und in das Feld c gepackt
for i in range (0, len(a), +1):
    c.append(a[i]+b[i])

print(c)


#Aufgabenteil 3
#Länge Polynom 1: 3
#Länge Polyon 2: 4
#Polyom 1: 2, 3, 4
#Polyom 2: 6, 1, 3, 8

# (2 + 3x + 4x**2) + (6 + 1x + 3x**2 + 8x**3)

pProduktListe = []
p1Liste = []
p2Liste = []

l1 = int(input("Geben Sie die Laenge vom 1. Polynom an! "))
l2 = int(input("Geben Sie die Laenge vom 2. Polynom an! "))


for i in range (l1 + 1):
    p1Liste += [int(input("Geben Sie den nächsten Koeffizienten des 1. Polynoms an! "))]
#    print (p1Liste)

for i in range (l2 + 1):
    p2Liste += [int(input("Geben Sie den nächsten Koeffizienten des 2. Polynoms an! "))]
#    print (p2Liste)

#x**0: pProduktListe[0] = [p1Liste[0] * p2Liste[0]]
#x**1: pProduktListe[1] = [p1Liste[0] * p2Liste[1] + p1Liste[1] * p2Liste[0]]
#x**2: pProduktListe[2] = [p1Liste[0] * p2Liste[2] + p1Liste[1] * p2Liste[1] + p1Liste[2] * p2Liste[0]]
#...

while len(pProduktListe) < (len(p1Liste) + len(p2Liste) - 1):
    pProduktListe += [0]

for i in range (len(p1Liste)):
    for j in range (len(p2Liste)):
        pProduktListe[i + j] += p1Liste[i] * p2Liste[j]

for i in pProduktListe:
    print (i)