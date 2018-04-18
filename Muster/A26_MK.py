class Rechteck:
    def __init__(self,cx,cy,l,b):
        self.cx = cx
        self.cy = cy
        self.l = l
        self.b = b

    def __str__(self):
        '''
        i = '[' + str(self.cx - self.b / 2) + '| ' + str(self.cx + self.b / 2) + ']' + ' x ' + '[' + str(self.cy - self.l / 2) + '| ' + str(self.cy + self.l / 2) + ']'
        '''
        i = '[%3.1f|%3.1f] x [%3.1f|%3.1f]' % (self.cx - self.b / 2, self.cx + self.b / 2, self.cy - self.l / 2, self.cy + self.l / 2)
        return i

    def rotiere(self):
        self.b,self.l = self.l,self.b
        return self

    def verschiebe(self, tx, ty):
        self.cx = self.cx + tx
        self.cy = self.cy + ty
        return self.cx, self.cy

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
        

    def flaeche(self):
        fl = self.l * self.b
        return fl
