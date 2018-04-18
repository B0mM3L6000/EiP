import math
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        p = '(' + str(self.x) + ', ' + str(self.y) + ')'
        return p

    def __lt__(self, other):
        return self.x < other.x

    def __eq__(self, other):
        if self.x == other.x:
            return self.y < other.y

    def abstand(self, other):
        d = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return d

def min_abstand(Punkte):                                                                                              
    min = math.sqrt((Punkte[1].x - Punkte[0].x) ** 2 + (Punkte[1].y - Punkte[0].y) ** 2)                          
    for zeile in range(len(Punkte)-1):                                                                                            
        d = math.sqrt((Punkte[zeile + 1].x - Punkte[zeile].x) ** 2 + (Punkte[zeile + 1].y - Punkte[zeile].y) ** 2)
        if d < min:                                                                                                   
            min = d                                                                                                   
            x = Punkte[zeile]                                                         
            y = Punkte[zeile + 1]                                                         
    return (x, y)                                                                                                     