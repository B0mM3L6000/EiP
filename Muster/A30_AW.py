class Knoten:
    def __init__(self, schluessel, kind1 = None, kind2 = None):
        self.s = schluessel
        self.k1 = kind1
        self.k2 = kind2

    c = []
    def suche(self, a, b):
        if self == None:
            return 0;
        else:
            if not self.s < a and not self.s > b:
                Knoten.c.append(self.s)
        return Knoten.suche(self.k1,a,b) * Knoten.suche(self.k2,a,b)


baum = Knoten(7,Knoten(1,Knoten(0),Knoten(3,Knoten(2),Knoten(5))),Knoten(12,Knoten(9,Knoten(8),Knoten(10)),Knoten(13,Knoten(15))))
Knoten.suche(baum, 4, 11)
print("c",Knoten.c)