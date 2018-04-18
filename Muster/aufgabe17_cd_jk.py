def ggT0(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def kuerze(a):
    g = ggT0(a[0], a[1])
    return (a[0] // g, a[1] // g)

def plus(a, b):
    c = (a[0] * b[1] + a[1] * b[0], a[1] * b[1])
    return kuerze(c)

def minus(a, b):
    c = (a[0] * b[1] - a[1] * b[0], a[1] * b[1])
    return kuerze(c)

def mal(a, b):
    c = (a[0] * b[0], a[1] * b[1])
    return kuerze(c)

def durch(a, b):
    c = (a[0] * b[1], a[1] * b[0])
    return kuerze(c)

#-------------------------------------------

def dif(f):
    diff = f[:] #Kopie von f
    for i in range (0, len(diff)):
        diff[i] = mal(diff[i],(i, 1))
    diff.remove(diff[0])
    return diff

def add(f,g):
    add1 = f[:]
    add2 = g[:]
    while len(add1) != len(add2):
        if len(add1) > len(add2):
            add2.append((0,1))
        else:
            add1.append((0,1))
    for i in range (0, len(add1)):
        add1[i] = plus(add1[i], add2[i])
    return add1

def sub(f,g):
    sub1 = f[:]
    sub2 = g[:]
    while len(sub1) != len(sub2):
        if len(sub1) > len(sub2):
            sub2.append((0,1))
        else:
            sub1.append((0,1))
    for i in range (0, len(sub1)):
        sub1[i] = minus(sub1[i], sub2[i])
    return sub1

def mul(f,g):
    mul1 = f[:]
    mul2 = g[:]
    add1 = []
    add2 = []
    for i in range (0, len(mul1)):
        for k in range (0, i):
            add1.append((0,1))
        for j in range (0, len(mul2)):
            add1.append(mal(mul1[i], mul2[j]))
        add2 = add(add1, add2)
        add1 = []
    return add2