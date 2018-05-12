#inputs

n = int(input("n ="))
k = 0     #k ist der Summenindex also startet bei 0


S1 = 0  #Summe
S2 = 0  #Summe Quadrate

for k in range(n+1):
    b = 1
    for i in range(k-1, -1, -1):
        b *= n-i
        b //= k-i

    #berechnen der Summe/Quadrate Summe:
    S1 +=b
    S2 +=b**2

print(S1,"und",S2)
