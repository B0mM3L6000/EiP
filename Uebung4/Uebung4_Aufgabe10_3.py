#Sauce header/input:

# Einlesen des Wertes von n
n = int(input())
# Einlesen von k entfaellt, da k der Summenindex ist
# Daher initialisierung als 0
k = 0
# Die Summe der Binomialkoeffizienten
S1 = 0
# Die Summe der Quadrate der Binomialkoeffizienten
S2 = 0


#Code:

for k in range(n+1):
    b = 1
    for i in range(k-1, -1, -1):
        b *= n-i
        b //= k-i

    #berechnen der Summe/Quadrate Summe:
    S1 +=b
    S2 +=b**2

#Sauce Output:

print("Summe k=0 bis",n ,"von", n, "ueber k =", S1)
print("Summe k=0 bis",n ,"der Quadrate von",n,"ueber k =", S2)


"""
Aufgabe 10.1:

n = 10
k = 5
b = 1

-> Schleife von 4 bis 0:

    i = 4:  b = 1 * (10-4) = 6
            b = 6 / (5-4) = 6
    i = 3:  b = 6 * (10-3) = 42
            b = 42 / (5-3) = 21
    i = 2:  b = 21 * (10-2) = 168
            b = 168 / (5-2) = 56
    i = 1:  b = 56 * (10-1) = 504
            b = 504 / (5-1) = 126
    i = 0:  b = 126 * (10-0) = 1260
            b = 1260 / (5-0) = 252

"""

"""
Aufgabe 10.2:

"""

"""
Aufgabe 10.3 (Beweiseteil):

"""
