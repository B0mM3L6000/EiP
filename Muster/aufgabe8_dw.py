n = int(input("n="))
k = 0           #Zähler
m = 2*n         #Zur Berechnung von 2n über n
l = n           #Zur Berechnung von 2n über n
e = 1           #Zur Berechnung von 2n über n

c = 0           #Zur Berechnung von S1
d = 0           #Zur Berechnung von S2

while k != n+1:

    b = 1

    for i in range(k - 1, -1, -1):  #Berechnung von S1 und S2
        b *= n - i
        b //= k - i

    c = c + b       #S1
    d = d + b*b     #S2
    k += 1

for i in range(l - 1, -1, -1):      #Berechnung von 2n über n
    e *= m - i
    e //= l - i

print("S1 =",c)
print("2^n =",2**n)
print ("S2 =",d)
print(m,"über",l,"=",e)