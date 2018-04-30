# Einlesen des Wertes R
R = float(input("Rate:"))
# Einlesen des Wertes p
p = float(input("Zins:"))
# Einlesen des Wertes n
n = float(input("Perioden:"))

#Variablen initialisieren:
K = 0
zaehler = int(n)
i = 1

#Perioden durchgehen und Raten einzahlen und dann verzinsen:
while i < zaehler+1:
    K = (K + R)*(1+p)
    i = i+1    #Erhöhen von i um 1 je Episode

#Ausgabe des Endkapitals
print(K)
