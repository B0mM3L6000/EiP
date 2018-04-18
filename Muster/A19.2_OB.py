def ggT(a,b):
    if a == 0:
        return b
    elif a%b == 0:
        return b
    else:
        return ggT(b,a%b)

memory = [[-1 for i in range(100)] for j in range(100)]
def binomial(n,k):
    if k > n:
        return -1
    elif k == 0 or k == n:
        return 1
    else:
        if memory[n-1][k-1] < 0:
            memory[n-1][k-1] = binomial(n-1,k-1)
        if memory[n-1][k] < 0:
            memory[n-1][k] = binomial(n-1,k)
        memory[n][k] = memory[n-1][k-1] + memory[n-1][k]
        return float(memory[n][k])

def sum(a,p):
    if p < 0 or p > len(a)-1:
        return 0
    elif p == len(a):
        return a[p]
    else:
        summe =  a[p] + sum(a,p+1)
        return summe

memmax = [-1 for i in range (100)]
def maximum(a,p):
    if p < 0:
        return -1
    elif p > len(a)-1:
        return maximum(a,len(a)-1)
    elif p == 0:
        return a[0]
    else:
        if memmax[p-1] < 0:
            memmax[p-1] = maximum(a,p-1)
        if memmax[p-1] < a[p]:
            memmax[p] = a[p]
        else:
            memmax[p] = memmax[p-1]
    return memmax[p]

def binaereSuche(a,wert,u,o):
    if wert == a[o]:
        return o
    if wert > a[o] or wert < a[u]:
        return -1
    elif u == o - 1 and a[u] < wert < a[o]:
        return -1
    else:
        mitte = (u + o) // 2
        if a[mitte] == wert:
            return mitte
        elif a[mitte] > wert:
            return binaereSuche(a,wert,u,mitte)
        else:
            return binaereSuche(a,wert,mitte,o)