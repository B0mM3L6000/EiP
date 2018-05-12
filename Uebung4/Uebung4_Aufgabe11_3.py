#sauce input:

# lies die Koeffizienten fuer Polynom 1 ein
a = [float(i) for i in (input().split())]
# lies die Koeffizienten fuer Polynom 2 ein
b = [float(i) for i in (input().split())]
# Initialisiere die Liste, die die Summe der Polynome beinhaltet
c = list()


#code:

maxexponent = len(a)+len(b)

#Initialisiere c mit maximal möglicher länger derliste nach polynomenmultiplikation (maximaler exponent b + exponent a + 1):
for _ in range(maxexponent):
    c.append(0)


#durchführen der polynomenmultiplikation
for i in range(len(a)):
    for j in range(len(b)):
        c[i+j] += a[i]*b[j]




#Sauce output:
print([float("%.2f" % k) for k in c])
