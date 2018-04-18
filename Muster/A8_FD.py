#Aufgabe 8.1.
n = int (input ("n = "))
k= int (input ("k = "))
b = 1
for i in range (k-1, -1, -1):
    b *= n-i
    b //= k-i
print(n, "über", k , "=",b)

#Wert für b: 1, 6, 42, 21, 168, 56, 504, 126, 1260, 252



#Aufgabe 8.3.
n = int (input ("n = "))
#k= Zähler
k = 0
m = 2*n #zur Berechnung von 2n über n
l = n #zur Berechnung von 2n über n
e = 1 #zur Berechnung von 2n über n
c = 0 #zur Berechnung von S1
d = 0 #zur Berechnung von S2
while k != n+1:
    b =1
    #Berechnung von S1 und S2:
    for i in range(k - 1, -1, -1):
        b *= n - i
        b //= k - i
    c = c + b #S1
    d = d + b*b #S2
    k += 1
#Berechnung von 2n über n
for i in range(l - 1, -1, -1):
    e *= m - i
    e //= l - i
print("S1 =",c)
print("2^n =", 2**n)
print("S2 =", d)
print(m, "über", l,"=", e)