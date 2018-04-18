# 1
def spur(a):
    s = 0
    for i in range(0, len(a)):
        for k in range(i, i + 1):
            s += a[i][k]
    return s


# 2
def spaltensummennorm(a):
    l = []
    for i in range(0, len(a)):
        summe = 0
        for k in range(0, len(a)):
            summe += abs(a[k][i])
        l.append(summe)
    c = max(l)
    return c


# 3 funktioniert jetzt richtig :)
def transponiere(a):
    for i in range(0, len(a) - 1):
        for k in range(i, len(a) - 1):
            a[i][k + 1], a[k + 1][i] = a[k + 1][i], a[i][k + 1]
    return a


# 4
def is_schiefsymmetrisch(a):
    l = []
    c = True
    for i in range(0, len(a)):
        if c == False:
            break
        for k in range(0, len(a)):
            if i == len(a) - 1 and k == len(a) - 1:
                l.append(True)
            if i == k:
                continue
            if a[i][k] == -(a[k][i]):
                continue
            else:
                l.append(False)
                c = False
                break
    return l[0]

