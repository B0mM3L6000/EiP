class Rechteck:
    def __init__(self,cx,cy,l,b):
        self.cx = cx
        self.cy = cy
        self.l = l
        self.b = b

    def __str__(self):
        self.bstart = self.cx-self.b/2
        self.bend = self.cx+self.b/2
        self.lstart = self.cy -self.l/2
        self.lend = self.cy+self.l/2

        return '[%.1f|%.1f] x [%.1f|%.1f]' %(self.bstart,self.bend,self.lstart,self.lend)


    def rotiere(self):
        self.b, self.l = self.l, self.b
        Rechteck.__str__(self)
        return

    def verschiebe(self,tx,ty):
        self.cx = self.cx + tx
        self.cy = self.cy + ty
        Rechteck.__str__(self)
        return

    def schnitt(self,other):
        if self.bstart> other.bend or self.bend < other.bstart:
            return None
        if self.lend < other.lstart or self.lstart>other.lend:
            return None
        else:
            Rechteck.__str__(self)
            Rechteck.__str__(other)
            self.bstart = max(self.bstart, other.bstart)
            self.bend = min(self.bend, other.bend)
            self.lstart = max(self.lstart, other.lstart)
            self.lend = min(self.lend, other.lend)
            return '[%.1f|%.1f] x [%.1f|%.1f]' % (self.bstart, self.bend, self.lstart, self.lend)


    def flaeche(self):
        return self.b*self.l