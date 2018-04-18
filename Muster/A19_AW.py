#Aufgabenteil 1
def ggT(a ,b):
    if b == 0:
        return a
    r = a % b
    return ggT(b, r)


#Aufgabenteil 2
n = 5
k = 3
mem = [-1 for i in range(n*(n+1)//2+k+1)]

def binomial(n,k):
    # Randstellen des Pascalschen Dreiecks
    if k == 0 or k == n:
        return 1
    #Berechnung des linken Vorgängers
    if mem[(n - 1) * n // 2 + k - 1] < 0:
        mem[(n - 1) * n // 2 + k - 1] = binomial(n-1, k-1)
    #Berechnung des rechten Vorgängers
    if mem[(n - 1) * n // 2 + k] < 0:
        mem[(n - 1) * n // 2 + k] = binomial(n-1, k)

    mem[n * (n + 1) // 2 + k] = mem[(n - 1) * n // 2 + k - 1] + mem[(n - 1) * n // 2 + k]
    return mem[n * (n + 1) // 2 + k]


#Aufgabenteil 3
def sum (a, p):
    if p > len(a):
        return 0
    if p == (len(a)-1):
         return a[len(a)-1]
    return a[p] + sum(a,p+1)


#Aufgabenteil 4
def maximum (a,p):
    if p > len(a):
        return 0
    if p == 0:
        return a[0]
    return max(a[p], maximum(a, p-1))


#Aufgabenteil 5
def binaereSuche(a,x,l,r):
    if l > r:
        return  -1
    middle = (l + r) // 2
    if a[middle] == x:
        return middle
    elif a[middle] > x:
        return binaereSuche(a,x,l,middle-1)
    else:
        return binaereSuche(a,x,middle+1,r)




a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("ggT =", ggT(24,18))
print("binKoeff =", binomial(n,k))
print(mem)
print("sum =", sum(a,6))
print("max =", maximum(a, 2))
print("binSuche =",binaereSuche(a,4,1,9))


