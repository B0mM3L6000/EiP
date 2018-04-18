# Aufgabe 9.1:
for a in range (1, 300):
    for b in range (a, 300): # Damit nicht (4,3) getestet wird
        c = a**2 + b**2
        c = c**(1/2)
        if c == int(c) and c < 300: # Prüfung auf Ganzzahl
            print(a,b,int(c))
            
# Aufgabe 9.2:
def calcGGT(a,b):
    while b != 0:
        r = a%b
        a=b
        b=r
    else:
        return(a)

countNum = 0
for a in range (1, 300):
    for b in range (a, 300):
        c = a**2 + b**2
        c = c**(1/2)
        if c == int(c) and c < 300:
            c = int(c)
            ggtAB = calcGGT(a, b)
            ggtAC = calcGGT(a, c)
            ggtBC = calcGGT(b, c)
            if ggtAB == ggtAC == ggtBC == 1:
                countNum +=1
                print(a,b,c)
print(countNum)

# Ergebnis: es gibt 47 solcher Tripel
