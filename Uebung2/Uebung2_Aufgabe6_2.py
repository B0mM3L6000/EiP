n = int(input("Welcher Wert für n?"))

i = 1
zeilenbreite = n + (n-1)

for _ in range(n):
    zeile = i+(i-1)
    zeilenseite = int((zeilenbreite - zeile)/2)
#    print(zeilenseite)
    print (zeilenseite*" ",end='')
    print (zeile*"0", end='')
    print (zeilenseite*" ")
    i = i + 1
