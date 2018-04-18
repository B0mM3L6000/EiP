import math

class Punkt:

    def __init__(self,xPunkt=0,yPunkt=0):
        self.x=xPunkt
        self.y=yPunkt

    def __str__(self):
        return '(%d, %d)' %(self.x,self.y)

    def __lt__(self,other):
        if self.x!=other.x:
            return self.x<other.x
        else:
            return self.y<other.y

    def sort(self):
        for i in range(0,len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]


    def abstand(self,other):
        if self==other:
            return 0
        if self<other:
            a=other.x-self.x
            if self.y<other.y:
                b=other.y-self.y
            else:
                b=self.y-other.y
        else:
            a=self.x-other.x
            if self.y<other.y:
                b=other.y-self.y
            else:
                b=self.y-other.y
        return math.sqrt(a**2+b**2)


import random
Punkte=[]
for i in range(0,5):
    P=random.randint(0,10)
    Q=random.randint(0,10)
    Punkte.append(Punkt(P,Q))

Punkte.sort()

def min_abstand(a):
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if Punkt.abstand(a[i],a[j])!=0:
                x=Punkt.abstand(a[i],a[j])
                break
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if Punkt.abstand(a[i],a[j])<x and a[i]!=a[j]:
                x=Punkt.abstand(a[i],a[j])
                p1=a[i]
                p2=a[j]
    return p1,p2