def ggT(a, b):
    if b==0:
        return a
    return ggT(b, a % b)

def binomial(n, k):
    if n < k:
        return -1
    if k == 0 or k == n: return 1
    if 2*k > n:
        result = binomial(n, n-k)
    else:
        result = n-k+1
        for i in range(2, k+1):
            result *= (n-k+i)
            result /= i
    return float(result)

def sum (a, p):
    if p > len(a):
        return 0
    if p == len(a):
        return 0
    else:
        return a[p] + sum(a, p+1)

def maximum(a,p):
    if p >= len(a):
        p = len(a)-1
    if p < 0:
        return -1
    elif p == 0:
        return a[0]
    else:
        previous = maximum(a,p-1)
        current = a[p]
        if previous > current:
            return previous
        else:
            return current

def binaereSuche(a, x, l, r):
    if r < l:
        return -1
    mitte = (l + r)//2
    if a[mitte] == x:
        return mitte
    elif a[mitte] < x:
        return binaereSuche(a, x, mitte+1, r)
    else:
        return binaereSuche(a, x, l, mitte-1)