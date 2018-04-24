# Einlesen des Wertes R
R = float(input("Rate:"))
# Einlesen des Wertes p
p = float(input("Zins:"))
# Einlesen des Wertes n
n = float(input("Perioden:"))

K = 0

zaehler = int(n)

for _ in range(1,zaehler+1):
    K = (K + R)*(1+p)

print("Endkapital:",K)
