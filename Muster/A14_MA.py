import random

#Aufgabenteil 1

a =[]
n = int(input("Länge von a: "))
for i in range (n):
    a.append(random.randint(0,n-1))

print(a)

#Aufgabenteil 2
a =[]
n = int(input("Länge von a: "))
for i in range (n):
    a.append(random.randint(0,n-1))


b  = []
v = 0
# Wir überprüfen wie viele der möglichen Elemente in a erhalten sind und zählen die Anzahl. Das ist die Anzahl der verschiedenen Elemente v in a.
for i in range(len(a)):
    if i in a:
        b.append(True)
        v += 1

    else:
        b.append(False)

print("Die Anzahl verschiedener Elemente v in a beträgt",v)

#Aufgabenteil 3
a = []
n = int(input("Länge von a: "))
for i in range(n):
    a.append(random.randint(0, n - 1))

a.sort()

# Nachdem wir a sortiert haben, überprüfen wir immer ein Element a[i] mit dem darauffolgenden Element a[i+1]. Wenn sie sich unterscheiden zählen wir v hoch und haben damit am Ende die Anzahl der unterschiedlichen Elemente v in a. Vorteil im Gegensatz zur Methode aus 2.) ist, dass wir kein neues Array anlegen müssen und somit keinen neuen Speicherplatz benötigen. Nachteil ist das wir a verändern mussten.

v2 = 1
z = a[0]
for i in range(1, len(a)):
    if (z != a[i]):
        v2 += 1
    z = a[i]
print(v2)