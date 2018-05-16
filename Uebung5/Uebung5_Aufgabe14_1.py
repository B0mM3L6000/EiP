#sauce head:

import random
# Die sortierte Liste
random.seed()
a = [random.randint(1,1000) for i in range(50)]
a.sort()

#Die zu suchende Zahl
x = int(input())

#Rueckgabe bei Erfolg
found = False



#CODE:


def suche(x, feld):
    gefunden = False
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

#ausführen:

found = suche(x, a)
#print(a)
#print(found)


#sauce footer:

if found == (x in a):
    print("correct!")
else:
    print("not correct!")
