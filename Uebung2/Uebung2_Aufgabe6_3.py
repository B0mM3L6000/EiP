n = int(input("Welcher Wert für n?"))

i = 1
zeilenbreite = n + (n-1)

for _ in range(n*2-1):
    if _ <= n-1:
        zeile = i+(i-1)
        zeilenseite = int((zeilenbreite - zeile)/2)
        print (zeilenseite*" ",end='')
        print (zeile*"0", end='')
        print (zeilenseite*" ")
        i = i + 1
    elif _ == n*2-2:
        print(zeilenbreite*"0")
    else:
        print ("0", end='')
        print ((zeilenbreite-2)*" ", end='')
        print ("0")


#könnte man auch für 6.4 direkt verwenden
