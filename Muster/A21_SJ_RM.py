"""
Sei n die Indexnummer des letzten Elements der Liste.
Im ersten Schritt werden die Elemente an den Stellen n und n-1 miteinander vertauscht.
Im 2. Schritt wird für jedes mögliche Ergebnis aus dem 1. Schritt die Elemente an den Stellen n-2 und n-1 vertauscht.
Im 3. Schritt wird für jedes mögliche Ergebnis aus dem 2. Schritt die Elemente an den Stellen n-3 und n-2 vertauscht.
usw...
Am Ende (am Anfang der Liste angekommen) ist jede mögliche Kombination der Elemente gebildet worden. Das Programm ist fertig.
"""

'''
Wahrscheinlichhkeit für i Felder weiterdrehen: (10-i) /45 für 1 <= i <= 9 und 0 sonst.
'''

a = [0,1,2,3,4,5,6,7,8,9]

wkeitSumme = 0

def permutation (a, p):
    if p == len(a)-1:
        print(a, wahrscheinlichkeitBerechnen(a))
#        print(wahrscheinlichkeitBerechnen(a))
        return

    for i in range (p, len(a)):
        a[p], a[i] = a[i], a[p]
        permutation(a, p+1)
        a[p], a[i] = a[i], a[p]
    print(wkeitSumme)

def wahrscheinlichkeitBerechnen (a):
    wahrscheinlichkeit = 1
    global wkeitSumme
    for i in range (0, len(a)-1):
        weitergedreht = a[i+1] - a[i]
        if weitergedreht < 0:
            weitergedreht += 10

            '''
            Bsp: von 9 auf 0 zu drehen bedeutet, ein Feld weiterzudrehen.
            Also: 0-9 = -9 < 0 => -9 + 10 = 1
            '''

            wahrscheinlichkeit = wahrscheinlichkeit * ((10 - weitergedreht)/45)

        elif (weitergedreht == 0) or (weitergedreht == 10):
            wahrscheinlichkeit = 0
        else:
            wahrscheinlichkeit = wahrscheinlichkeit * ((10 - weitergedreht) / 45)
    wkeitSumme += wahrscheinlichkeit
    return wahrscheinlichkeit


permutation (a, 0)
print(wkeitSumme)