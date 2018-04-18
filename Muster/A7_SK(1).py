#Aufgabenteil 1
Zaehler=0
n = int (input("n = "))

while n > 1:
    Zaehler += 1
    print (Zaehler,": ", n)
    if n%2 == 0:
        n=n//2
    else:
        n=n*3+1

#Aufgabenteil 2
n = 2367363789863971985761
Zaehler = 1
while n != 1:
    if n%2 != 0:
        n = 3 * n + 1
    else:
        n = n // 2
    Zaehler += 1
print (Zaehler)

#Aufgabenteil 3
g = 1000000
maxZähler = 0

for n in range (1,g):
    Zähler = 1
    n0 = n
    while n0 != 1:
        if n0%2 != 0:
            n0 = 3 * n0 + 1
        else:
            n0 = n0 // 2
        Zähler += 1
    if Zähler > maxZähler:
        maxZähler = Zähler
        maxn = n
print ("Längste Startzahl = ",maxn," , mit einer Folgenlänge von ", maxZähler)