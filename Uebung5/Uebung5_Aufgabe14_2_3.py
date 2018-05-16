#sauce head:

import random
# Die sortierte Liste
random.seed()
a = [random.randint(1,1000) for i in range(50)]
a.sort()

#Die zu suchende Range
unten = int(input())
oben = int(input())

#Rueckgabe der Range
numElements = 0



#CODE:


def suche(x, feld1):
    gefunden = False
    feld = feld1
    #print(len(feld))
    n = len(feld)
    #print("Längefeld:",n)
    if n%2 == 0:
        n = n//2
    else:
        n = (n+1)//2
    #print(n)
    #print("elementwert:", feld[n-1])
    #testen ob stelle n-1 (wegen index 0 bis len(feld)-1) die gesuchte zahl ist:
    if feld[n-1] == x:
        gefunden = True
        #print("gefunden")
    #testen ob das feld vollständig durchsucht wurde:
    elif n <=1:
        gefunden = False
    #rekursiv mit neuem feld je nachdem ob x kleiner oder größer feld[n-1]
    elif feld[n-1] > x:
        feld = feld[0:n]
        #print("länge neues feld:", len(feld))
        #print("x ist kleiner",feld)
        gefunden = suche(x,feld)
    elif feld[n-1] < x:
        feld = feld[n:len(feld)]
        #print("länge neues feld:", len(feld))
        #print("x ist größer", feld)
        gefunden = suche(x, feld)
    return gefunden


#anpassung für intervall:

def intervallsucheeinzigartig(unten, oben, feld2):
    intervall = list(range(unten, oben+1))
    zaehler = 0
    for i in range(len(intervall)):
        #print(intervall[i])
        gefunden = suche(intervall[i], feld2)
        if gefunden == True:
            zaehler += 1
            #print(zaehler)
    #print(intervall)
    #print(zaehler)
    return zaehler

"""
Problem hier ist, dass er nur die Anzahl der einzigartigen Elemente testet.
Muss noch so ergänz werden, dass er nochmal testet ob in dem feld ein weiterer
Wert mit der selben Zahl ist.

Daher:
"""

def intervallsucheabsolut(unten, oben, feld2):
    intervall = list(range(unten, oben+1))
    zaehler = 0
    for i in range(len(intervall)):
        for j in range(len(feld2)):
            if intervall[i] == feld2[j]:
                zaehler += 1
            if intervall[i] < feld2[j]:
                break
    return zaehler

#ausführen:


numElements = intervallsucheabsolut(unten, oben, a)
#testlist = set(a)
#print(len(testlist))


#sauce footer:

if numElements == sum([1 for x in a if (x>=unten and x<=oben) ]):
    print("correct!")
else:
    print("not correct!")
    print("correct answer", sum([1 for x in a if (x>=unten and x<=oben) ]))
    print(a)





"""

Aufgabe 14.3:





"""
