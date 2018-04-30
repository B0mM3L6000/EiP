n = int(input("Welcher Wert für n?"))

j = 0
i = 1
zeilenbreite = n + (n-1)

while j < n:
    zeile = i+(i-1)
    zeilenseite = int((zeilenbreite - zeile)/2)
    print (zeilenseite*" ",end='')
    print (zeile*"0", end='')
    print (zeilenseite*" ")
    i = i + 1
    j = j+1
