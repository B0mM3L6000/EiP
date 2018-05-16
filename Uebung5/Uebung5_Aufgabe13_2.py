#sauce head:
length = int(input())
b = list()


#CODE:


#berechnung Binomialkoeffizienten

def binom(n, k):
    b = 1
    for i in range(k-1, -1, -1):
        b *= n-i
        b //= k-i
    return b

#erzeugen des felds:

def pascal_d(n):
    output = list()
    for zeile in range(n):
        for spalte in range(zeile+1):
            #print("zeile:", zeile, "spalte:", spalte)
            output.append(binom(zeile, spalte))
            #print(tmp)
    return output



#ausführen:

b = pascal_d(length)
#print(b)




#sauce footer:

c = [[b[i+((y-1)*(y))//2] for i in range(y)] for y in range(1,length+1)]
correct = (len(c)==length)
for i in range(len(c)):
    correct = correct and (len(c[i]) == i+1)
    for j in range(len(c[i])):
        if(j==0 or j==(len(c[i])-1)):
            correct = correct and c[i][j] == 1
        else:
            correct = (correct and (c[i][j] == c[i-1][j-1]+c[i-1][j]))

if correct:
    print("correct!")
else:
    print("not correct!")
    print("your solution:")
    print(b)



"""
Welche Länge muss das Feld besitzen?

Antwort:

Summe (von i = 1 bis n) [ i ]

_______________________________________________________________________


Aufgabe 13.3:

n*(n+1)/2 + k = Sum(von i=0 bis n)[i]   +   k

Dies summiert immer die Anzahl der Elemente in einer Zeile des Pascalchen
Dreieck auf. Da man in Listen bei 0 anfängt die Indexe zu zählen, statt bei 1,
ist man so immer bei dem 1. Element der Zeile. Addiert man nun k auf dieses Element,
so landet man genau bei dem Element k in zeile n also dem Binomialkoeffizienten
n über k (k bei 0 anfangen zu zählen).
Da das eindimensionale Feld nichts anderes ist, als das Pascalche Dreieck in einer
Reihe aufgeschrieben, stimmt die Aussage aus 13.3

"""
