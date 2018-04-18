#Achtung, hier wird der Schnitt zwischen den Vierecken berechnet, da dies in Sauce auch getan wurde. Eigentlich wurde aber nach der Vereinigung gefragt!

class Punkt:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rechteck:
    def __init__(self, cx, cy, l, b):
        self.x = cx
        self.y = cy
        self.l = l
        self.b = b

    def schnitt(self, other):
        sux = self.x - 0.5 * self.b
        sox = self.x + 0.5 * self.b
        suy = self.y - 0.5 * self.l
        soy = self.y + 0.5 * self.l

        oux = other.x - 0.5 * other.b
        oox = other.x + 0.5 * other.b
        ouy = other.y - 0.5 * other.l
        ooy = other.y + 0.5 * other.l

        if sux > oox:
            return None
        if sox < oux:
            return None
        if soy < ouy:
            return None
        if suy > ooy:
            return None
        if sux > oox:
            return None
        if sox < oux:
            return None
        if soy < ouy:
            return None
        if suy > ooy:
            return None

        if suy < ouy:
            uy = ouy
        else:
            uy = suy
        if soy < ooy:
            oy = soy
        else:
            oy = ooy
        if sux < oux:
            ux = oux
        else:
            ux = sux
        if sox < oox:
            ox = sox
        else:
            ox = oox
        l = oy - uy
        b = ox - ux
        cy = uy + 0.5 * l
        cx = ux + 0.5 * b
        return Rechteck(cx, cy, l, b)

    def flaeche(self):
        return self.l * self.b

def outside_number (p, r):
    z = 0
    for i in range (0, len(p)):
        x = p[i].x
        y = p[i].y
        for j in range (0, len(r)):
            ux = r[j].x - 0.5 * r[j].b
            ox = r[j].x + 0.5 * r[j].b
            oy = r[j].y + 0.5 * r[j].l
            uy = r[j].y - 0.5 * r[j].l
            if x > ux and x < ox and y > uy and y < oy:
                z += 1
                break
    z = len(p) - z
    return z

def flaeche_2(a):
    r1 = a[0]
    r2 = a[1]
    return r1.schnitt(r2).flaeche()
# Das ist aber die Flaeche des Schnittrechtecks!
# Die richtige Flaeche (Vereinigung) würde mit return r1.flaeche() + r2.flaeche() - r1.schnitt(r2).flaeche() zurueckgegeben

def flaeche_3(a):
    s1 = a[0].schnitt(a[1])
    s2 = a[1].schnitt(a[2])
    return s1.schnitt(s2).flaeche()

"""
Wenn man Feld mit x Rechtecken hat, dann hat man x-1 Schnittrechtecke. Diese kann man wieder in einem neuen Feld abspeichern,
mit dem man dann wieder die Funktion aufruft. Dieses Feld hat dass wieder x-1 Schnittrechtecke, mit der man dann immer wieder
die Funktion rekursiv aufrufen kann. Das Rekursionsende ist erreicht, wenn das Feld, mit dem die Funktion aufgerufen wird nur ein
Rechteck beinhaltet. Dann kann man davon die Flaeche berechnen und zurückgeben.
"""

def flaeche_n(p):
    if len(p) == 1:
        return p[0].flaeche()
    a = []
    for i in range (0, len(p)-1):
        r = p[i].schnitt(p[i+1])
        if r == None:
            return 0
    return flaeche_n(a)