import math

#gesucht alle Primzahlpaare zwischen 10101 und 10901

#Array aller Primzahlen (hier werden neue Primzahlen abgespeichert) initialsiert mit 2
primzahlen = [2]

#Array aller Primzahlpaare
primzahlpaare = []

# überrüfen welche zahlen primzahlen sind durch teilen der zahlen 2 bis p durch alle primzahlen
# im raum 2 bis sqrt(p) und überprüfen ob ein Rest vorliegt mithilfe des modulo

lowerbound = int(input("Ab welcher Zahl soll geprüft werden?"))

while lowerbound <= 2:
    lowerbound = int(input("Bitte eine Zahl größer als 2 eingeben. Danke."))

p = int(input("Bis zu welcher Zahl soll geprüft werden?"))

for zahl in range(2, p):
    check = True
    #print(primzahlen)    #zu testzwecken
    i = 0
    teiler = primzahlen[i]

    while teiler <= math.sqrt(zahl) and len(primzahlen) >= (i+1):
        if (zahl%teiler) == 0:
            #print(zahl, "ist keine Primzahl.")     #zu testzwecken
            check = False
            break

        else:
            i = i+1
            teiler = primzahlen[i]

    if check == True:
        #print(zahl, "ist eine Primzahl")    #zu testzwecken
        primzahlen.append(zahl)
        if zahl < lowerbound:
            grenze = len(primzahlen)


#print(primzahlen)    #zu testzwecken

#print(grenze)   #zu testzwecken

# Überprüfen ob Primzahlpaar vorliegt im Raum lowerbound bis p durch berechnen der
# Diffrenz der nebeneinander liegended Primzahlen

#dazu zunächst alle Primzahlen aus dem nicht zu testenden Bereich entfernen

for _ in range(grenze):
    primzahlen.remove(primzahlen[0])

#print(primzahlen)     # zu testzwecken

#jetzt Diffrenz bilden und Primzahlpaare abspeichern

for j in range(len(primzahlen)-1):
    if (primzahlen[j+1] - primzahlen[j]) == 2:
        #print (primzahlen[j], "und", primzahlen[j+1], "sind ein Primzahlpaar")
        primzahlpaare.append((primzahlen[j], primzahlen[j+1]))


print("Im durchsuchten Raum existieren folgende Primzahlpaare:",primzahlpaare)
