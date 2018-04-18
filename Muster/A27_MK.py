class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        p = '(' + str(self.x) + ', ' + str(self.y) + ')'
        return p

class Rechteck:
    def __init__(self,cx,cy,l,b):
        self.cx = cx
        self.cy = cy
        self.l = l
        self.b = b

    def __str__(self):
        i = '[' + str(self.cx - self.b / 2) + ', ' + str(self.cx + self.b / 2) + ']' + 'x' + '[' + str(self.cy - self.l / 2) + ', ' + str(self.cy + self.l / 2) + ']'
        return i
        
    def schnitt(self, other):
        sux = self.cx - self.b / 2
        sox = self.cx + self.b / 2
        suy = self.cy - self.l / 2
        soy = self.cy + self.l / 2
        oux = other.cx - other.b / 2
        oox = other.cx + other.b / 2
        ouy = other.cy - other.l / 2
        ooy = other.cy + other.l / 2
        if self.cx < other.cx:
            schnittcx = oux + (sox - oux) / 2
            schnittb = sox - oux
        else:
            schnittcx = sux + (oox - sux) / 2
            schnittb = oox - sux
        if self.cy < other.cy:
            schnittcy = ouy + (soy - ouy) / 2
            schnittl = soy - ouy
        else:
            schnittcy = suy + (ooy - suy) / 2
            schnittl = ooy - suy
        if sox >= oox and sux <= oux:
            schnittcx = other.cx
            schnittb = other.b
        elif oox >= sox and oux <= sux:
            schnittcx = self.cx
            schnittb = self.b
        if soy >= ooy and suy <= ouy:
            schnittcy = other.cy
            schnittl = other.l
        elif ooy >= soy and ouy <= suy:
            schnittcy = self.cy
            schnittl = self.l
        if schnittl >= 0 and schnittb >= 0:
            return Rechteck(schnittcx, schnittcy, schnittl, schnittb)
        return Rechteck(0, 0, 0, 0)


    def flaeche(self):
        fl = self.l * self.b
        return fl

def outside_number(Punkte, Rechtecke):
    out = 0
    for j in range(len(Punkte)):
        drin = False
        for i in range(len(Rechtecke)):
            if Punkte[j].x > Rechtecke[i].cx - Rechtecke[i].b / 2 and Punkte[j].x < Rechtecke[i].cx + Rechtecke[i].b / 2:
                if Punkte[j].y > Rechtecke[i].cy - Rechtecke[i].l/ 2 and Punkte[j].y < Rechtecke[i].cy + Rechtecke[i].l / 2:
                    drin = True
                    break
        if drin == False:
            out += 1
    return out
    
def flaeche_2(a):
    '''
    Der eigentliche Flächeninhalt von zwei vereinigten Gebieten wird eigentlich wie folgt berechnet:
    fl2 = a[0].flaeche() + a[1].flaeche() - (a[0].schnitt(a[1])).flaeche()
    Sauce verlangt jedoch den Flächeninhalt der Schnittmenge?
    '''
    return a[0].schnitt(a[1]).flaeche()
    
def flaeche_3(a):
    #Anscheinend ist wieder die Fläche der gemeinsamen Schnittmenge gefragt:
    return a[0].schnitt(a[1]).schnitt(a[2]).flaeche()
    
def rek(a, z):
    if z <= 0:
        return a[0]
    return a[z].schnitt(rek(a, z-1))

def flaeche_n(a):
    z = len(a)-1
    return rek(a, z).flaeche()

