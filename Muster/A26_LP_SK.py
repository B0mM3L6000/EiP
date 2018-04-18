#Damit die Ausgabe dieses Codes mit der Lösung in Sauce übereinstimmt, müssen l und b vertauscht werden
class Rechteck:
    def __init__(self,cx=0,cy=0,l=0,b=0):
        self.cx=cx  ##########################
        self.cy=cy  #Mittelpunkt,Breite,Hoehe
        self.l=l    #zuweisen
        self.b=b    ##########################
        self.ux=cx-l/2  #######################
        self.ox=cx+l/2  #Intervallgrenzen zuweisen
        self.uy=cy-b/2  #
        self.oy=cy+b/2  #######################
    def __str__(self):
        #Intervalldarstellung mit 2 Nachkommastellen
        return '[%.2f,%.2f]x[%.2f,%.2f]' %(self.ux,self.ox,self.uy,self.oy)
    def rotiere(self):
        #Laenge und Breite vertauschen
        return Rechteck(self.cx,self.cy,self.b,self.l)
    def verschiebe(self,tx,ty):
        #Mittelpunkt verschieben
        return Rechteck(self.cx+tx,self.cy+ty,self.l,self.b)
    def schnitt(self,other):
        if self.ox<other.ux or other.ox<self.ux:#Schnitt in x-Richtung?
            return Rechteck()#kein Schnitt gebe das 0-Rechteck zurueck
        if self.oy<other.uy or other.oy<self.uy:#Schnitt in y-Richtung?
            return Rechteck()#kein Schnitt gebe das 0-Rechteck zurueck
        neuux=max(self.ux,other.ux)###################################
        neuox=min(self.ox,other.ox)#neue Intervallgrenzen:neue untere grenze ist max der alten
        neuuy=max(self.uy,other.uy)#                      neue obere grenze ist min der alten
        neuoy=min(self.oy,other.oy)###################################
        neucx=(neuux+neuox)/2###################
        neucy=(neuuy+neuoy)/2#neue Mitte = (untere grenze + obere Grenze)/2
        neul=neuox-neuux#######################
        neub=neuoy-neuuy#neue abmessung = obere grenze - untere grenze
        return Rechteck(neucx,neucy,neul,neub)
    def flaeche(self):
        return self.l*self.b#A = laenge * breite