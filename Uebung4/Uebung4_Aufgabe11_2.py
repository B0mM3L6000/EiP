#sauce input:

# lies die Koeffizienten fuer Polynom 1 ein
a = [float(i) for i in (input().split())]
# lies die Koeffizienten fuer Polynom 2 ein
b = [float(i) for i in (input().split())]
# Initialisiere die Liste, die die Summe der Polynome beinhaltet
c = list()


#code:

#anpassen der Laenge der listen:
if len(a) > len(b):
    dif = len(a) - len(b)
    for _  in range(dif):
        b.append(0)
elif len(b) > len(a):
    dif = len(b) - len(a)
    for _ in range(dif):
        a.append(0)


for j in range(len(a)):
    c.append(a[j] + b[j])


#sauce output:
print(c)
