class Vektor:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        c = Vektor(self.x + other.x, self.y + other.y, self.z + other.z)
        return c

    def __sub__(self,other):
        c = Vektor(self.x - other.x, self.y - other.y, self.z - other.z)
        return c

    def __mul__(self,other):
        c = self.x*other.x+self.y*other.y+self.z*other.z
        return c

    def __lt__(self,other):
        return (self.x**2+self.y**2+self.z**2)**0.5 < (other.x**2+other.y**2+other.z**2)**0.5


a = Vektor(1,2,3)
b = Vektor(3,2,1)

print(a.x,a.y,a.z)

a = a*b

print(a)