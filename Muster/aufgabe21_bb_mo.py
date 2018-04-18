h=[]
h3=0
def permutation(a,p):
    if p==len(a)-1:
        if a[0]!=0:
            x3 = 1
            for j in range(0, len(a) - 1):
                if j == 0:
                    x1 = a[0]
                    x2 = ((10 - x1) / 45)
                    x3 = x2 * x3
                if a[j + 1] > a[j]:
                    x1 = a[j + 1] - a[j]
                    x2 = ((10 - x1) / 45)
                    x3 = x2 * x3
                if a[j] > a[j + 1]:
                    x1 = 10 - a[j] + a[j + 1]
                    x2 = ((10 - x1) / 45)
                    x3 = x2 * x3
            h.append(x3)
            return 
    for i in range (p,len(a)):
        a[p],a[i]=a[i],a[p]
        permutation(a,p+1)
        a[p],a[i]=a[i],a[p]
a=[0,1,2,3,4,5,6,7,8,9]
print (permutation(a,0))
for x in h:
    h3+=x
print(h3)



"""
Da die Permutationen von hinten nach vorne vorgenommen werden betrachten wir die Permutation einmal für p = 8:
Da p=8 != len(a)-1 gehen wir in die for-Schleife. hier wird nun a[8] mit a[8] vertauscht,
bleibt also gleich (123456789), dann ruft es die Permutationen für p=9 unseres aktuellen a
auf. Permutation wird aufgerufen: permutation(a, 9)
Da len(a)-1 = 9 wird unsere Permutation ausgegeben -> print(123456789)
jetzt gehen wir zurück in permutation(a,8). Die Positionen a[8],a[8] werden zurückgetauscht,
bleiben also wieder gleich. i wird auf 9 erhöht und a[8] mit a[9] vertauscht (123456798).
Nun wir wieder Permutation(a,9) aufgerufen, diesmal aber mit unserem verändertem a
len(a)-1 = 9 daher wird a ausgegeben -> print(123456798)
Wir gehen zurück in Permutatuin(a,8) und a[8],a[9] werden zurückgetauscht (123456789).
Die for-Schleife ist am Ende und das Programm wird beendet. Alle Permutationen wurden ausgegeben.
Dies funktioniert nun natürlich auch wenn wir p niedriger machen bis hin zu p=0 wobei
wir dann n! Permutationen haben.
Bei p=7 würde somit zunächst nichts vertauscht -> Ausgabe(123456789), dann innerhalb von 
Permutation(a,8) vertauscht und Ausgabe (123456798), dann wird zurück permutiert zu
(123456789), wir gehen zurück in permutation(a,7), i wird auf 8 erhöht, es wird a[7],a[8]
vertauscht (123456879) -> in der inneren Funktion selbes Prinzip wie zuvor 
-> Ausgabe (123456879) und (123456897) -> Permutation wird wieder zu (123456789) und 
i auf 9 erhöht ->  vertauschen von a[7] und a[9] (123456987) -> innen wieder selbiges
Prinzip -> Ausgabe (123456987) und (123456978) -> zurücktauschen zu (123456789) ->Ende 
-> Wie allgemein formuliert haben wir 3! = 6 Permutationen


"""
