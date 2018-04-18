#Aufgabenteil 1

#  McCarthy Funktion
def f(n):
    if n > 100:
        return n-10
    if n <= 100:
        return (f(f(n+11)))

print (f(1000))


#Aufgabenteil 2

#Ackerman-Funktion
def a(k, n):
    if n == 1:
        return 2
    if k == 1:
        return 2*n
    return a(k-1, a(k,n-1))

print (a(2, 1))