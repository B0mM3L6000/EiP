# Einlesen des Wertes R
R = float(input("Rate:"))
# Einlesen des Wertes p
p = float(input("Zins:"))
# Einlesen des Wertes n
n = float(input("Perioden:"))

K = 0

zaehler = int(n)
i = 1

while i < zaehler+1:
    K = (K + R)*(1+p)
    i = i+1

print("Endkapital:",K)
