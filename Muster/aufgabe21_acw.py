def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


def permutation(a, p):
    global gewinn_wsk
    if p == len(a) - 1:
        if a[0] != 1:
            wsk = berechne_wsk(a)
            gewinn_wsk += wsk
        return
    for i in range(p, len(a)):
        a[p], a[i] = a[i], a[p]
        permutation(a, p + 1)
        a[p], a[i] = a[i], a[p]


def berechne_wsk(p):
    a = len(p)
    teiler = sum(range(1, a))
    wsk = (a - (p[0] - 1)) / teiler
    for j in range(len(p) - 1):
        differenz = (p[j + 1] - p[j]) % a
        wsk *= (a - differenz) / teiler
    return wsk


gewinn_wsk = 0
permutation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
print("Gewinn:", gewinn_wsk)
