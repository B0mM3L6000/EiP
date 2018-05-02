n = int(input("Welche Startzahl für die Collatz Folge?"))

#überprüfen welche länge n = 2367363789863971985761 hat
#print(n)
i = 1

while n != 1:   #solange n noch nicht gleich 1 ist
    if n%2 == 0:    #wenn n durch 2 ganz teilbar ist
        n = n//2
        #print(n)
    else:     #ansonsten
        n = n*3+1
        #print(n)

    i = i+1


print("Die Länge der Folge ist:",i)




"""
 Hier muss noch in die Kommentare wie man die Zahl n findet welches die möglichst
 längste Folge hat für n < 10^6. Mit Worten erklärt.

 """
