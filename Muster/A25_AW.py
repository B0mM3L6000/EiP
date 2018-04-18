import random

class Punkt:

    #Aufgabenteil 1
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def __str__(self):
        return '(' + str(self.x) +','+ str(self.y)+')'


    #Aufgabenteil 2
    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x and self.y < other.y:
            return True
        else:
            return False


    #Aufgabenteil 4
    def abstand(self, other2):
        return ((other2.x-self.x)**2 + (other2.y - self.y)**2)**(1/2)


    #Aufgabenteil 5
    def minAbstand(a):
        min = 10000000
        tmp1 = -1
        tmp2 = -1
        for i in range (len(a)):
            for j in range (0, i):
                if i == j:
                    continue
                if Punkt.abstand(a[i],a[j]) < min:
                    min = Punkt.abstand(a[i],a[j])
                    tmp1 = i
                    tmp2 = j
        return a[tmp1], a[tmp2]






Punkte = []
for i in range (10):
    Punkte.append(Punkt(random.randint(1,10),random.randint(1,10)))
    print(Punkte[i])


p = [(8199, 3721), (541, 8752), (2939, 9121), (90, 7195), (326, 9157), (7631, 5562), (6304, 3144), (4271, 2938), (9544, 57), (8624, 8859), (2060, 1794), (646, 3078), (7186, 2509), (338, 3693), (9756, 3964), (620, 5532), (1469, 9407), (9860, 700), (470, 2324), (5662, 1962), (2704, 7834), (2553, 6270), (3547, 2960), (3926, 6870), (9830, 7194), (4179, 4857), (3128, 4046), (5018, 6623), (1041, 297), (8628, 2256), (2532, 6208), (6772, 6440), (9919, 7316), (8982, 8627), (8131, 7762), (7204, 9780), (9052, 7097), (4418, 7629), (1502, 5035), (811, 157), (6053, 7665), (7574, 5898), (8763, 8710), (292, 1562), (7625, 6424), (8698, 1967), (6290, 4861), (1315, 6678), (2897, 1038), (632, 6178), (4642, 7460), (8935, 1018), (3438, 1715), (7992, 5727), (4973, 2509), (8766, 3815), (4976, 4004), (7079, 1116), (2901, 6913), (6828, 5657), (2719, 5305), (8777, 3226), (3600, 1944), (7189, 865), (231, 2586), (2221, 5023), (5413, 4220), (3890, 3722), (8802, 3202), (5441, 1539), (848, 3973), (7966, 1944), (8714, 2629), (5708, 152), (4239, 5756), (3392, 2722), (1024, 954), (765, 2971), (6313, 2452), (2816, 7523), (8239, 1961), (6405, 2599), (9738, 3852), (2900, 2619), (4187, 1328), (9532, 4819), (3303, 9131), (9451, 8284), (9008, 9928), (2382, 4614), (2480, 2643), (2432, 3958), (3362, 7504), (4856, 3561), (6449, 1239), (7619, 7368), (6480, 4608), (3949, 1828), (218, 1788), (1354, 1092), (9555, 4291), (9510, 2083), (196, 3898), (8341, 6158), (4720, 644), (7991, 6351), (8594, 1220), (8073, 816), (2033, 3600), (8205, 6187), (7858, 2552), (5866, 8760), (3351, 9933), (2027, 4504), (5567, 4371), (659, 8652), (4682, 7202), (7606, 7752), (8922, 2978), (43, 2142), (6162, 2197), (1654, 3354), (9023, 2466), (477, 3986), (9599, 1185), (2662, 9535), (4203, 3489), (7792, 5499), (896, 1798), (3692, 9361), (9218, 9796), (6133, 1796), (2643, 6875), (9410, 9037), (8197, 7093), (1237, 8098), (2748, 6032), (9915, 8207), (5294, 2033), (6330, 407), (3001, 3853), (7738, 8961)]
Punkte = []     # Feld mit zufälligen Punkten
for i in p:
    Punkte.append(Punkt(i[0], i[1]))

Punkte.sort()   # Feld sortieren


a,b = Punkt.minAbstand(Punkte)
print(a,b)

