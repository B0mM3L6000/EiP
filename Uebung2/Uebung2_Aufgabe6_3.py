n = int(input("Welcher Wert für n?"))

j = 0
i = 1
zeilenbreite = n + (n-1)

while j < (n*2-1):
    if j <= n-1:    #dach wird hier gemacht
        zeile = i+(i-1)
        zeilenseite = int((zeilenbreite - zeile)/2)
        print (zeilenseite*" ",end='')
        print (zeile*"0", end='')
        print (zeilenseite*" ")
        i = i + 1
    elif j == n*2-2:     #"Boden" wird hier gemacht
        print(zeilenbreite*"0")
    else:     #Mitte wird hier gemacht
        print ("0", end='')
        print ((zeilenbreite-2)*" ", end='')
        print ("0")
    j = j+1
