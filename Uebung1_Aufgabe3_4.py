# p gesucht

K = float(input("Wie hoch ist das Endkapital?"))
K0 = float(input("Wie hoch ist das Startkapital?"))
n = float(input("Wieviele Perioden hast du angelegt?"))

# Berechnung:
# n-Wurzel(K/K0)- 1 = p

p = ((K/K0))**(1/n) - 1

p = round(p,2)

print("Der Zinssatz beträgt ", p, ".")
