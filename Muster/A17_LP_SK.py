###################BRUCHRECHNEN##################################
def ggT(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def kuerze(a):
    g = ggT(a[0], a[1])
    return (a[0] // g, a[1] // g)


def addtup(a, b):
    c = (a[0] * b[1] + a[1] * b[0], a[1] * b[1])
    return kuerze(c)


def subtup(a, b):
    c = (a[0] * b[1] - a[1] * b[0], a[1] * b[1])
    return kuerze(c)


def multup(a, b):
    c = (a[0] * b[0], a[1] * b[1])
    return kuerze(c)


def divtup(a, b):
    c = (a[0] * b[1], a[1] * b[0])
    return kuerze(c)
###################################################################################
#########################ANFANG DER AUFGABE########################################
def dif(f):
    c=[]
    for x in range (0,len(f)-1):
        c.append(multup(f[x+1],(x+1,1)))
    return c

def add(f,g):
    c=[]
    while len(f)!=len(g):
        if len(f)>len(g):
            g.append((0,1))
        else:
            f.append((0,1))
    for y in range(len(f)):
        c.append(addtup(f[y],g[y]))
    return c

def sub(f,g):
    c=[]
    while len(f)!=len(g):
        if len(f)>len(g):
            g.append((0,1))
        else:
            f.append((0,1))
    for y in range(len(f)):
        c.append(subtup(f[y],g[y]))
    return c

def mul(f,g):
    c=[]
    ende=len(f)+len(g)-1#neues polynom hat diesen grad -1

    for i in range (0,ende):#schleife aussen für die einzelnen c[i]
        sum=(0,1)
        for j in range (0,len(f)):#erzeuge alle kombinationen der indizes von a und b...
            for k in range (0,len(g)):
                if j+k == i:#...und lasse nur diejenigen zu die in der summe gleich der zu berechnenden potenz sind
                    sum=addtup(sum,multup(f[j],g[k]))
        c.append(sum)
    return c

def div(f,g):
    erg=[]
    erg2=[]
    r=f
    while len(g)<=len(r):#solange der rest noch teilbar ist
        c=[]
        x=len(r)-len(g)
        for y in range(x):                              #erzeuge die potenz um die g erweitert wird
            c.append((0,1))                             #indem bis zur gewuenschten potenz 0en angehängt werden
        c.append(divtup(r[len(r)-1],g[len(g)-1]))       #erzeuge den faktor
        erg.append(c[len(c)-1])                         #und speichere das zwischenergebnis
        c=mul(c,g)                                      #erweitere g um diese potenz*faktor
        r=sub(r,c)                                      #damit wir c von r subtrahieren
        r.pop()                                         #entferne eine null sodass die aeussere while schleife ein ende findet
    for i in reversed(erg):                             #aufgrund der vorgehensweise hat erg die falsche
        erg2.append(i)                                  #reihenfolge und das korrigieren wir jetzt
    return erg2,r