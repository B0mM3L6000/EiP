n = int(input("Welche Startzahl für die Collatz Folge?"))

print(n)

while n != 1:   #solange n noch nicht gleich 1 ist
    if n%2 == 0:    #wenn n durch 2 ganz teilbar ist
        n = n//2
        print(n)
    else:     #ansonsten
        n = n*3+1
        print(n)
