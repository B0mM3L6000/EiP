import random

class Skatspiel:
    def __init__(self):
        self.kartenstapel = list(range(1,33))
        self.spieler1 = []
        self.spieler2 = []
        self.spieler3 = []
        self.skat = []


    def __str__(self):
        return str(self.kartenstapel)+ '\n' + 'Spieler 1: '+ str(self.spieler1) + '\n' + 'Spieler 2: '+ str(self.spieler2) + '\n' + 'Spieler 3: '+ str(self.spieler3) + '\n' + 'Skat: '+ str(self.skat)

    def mischen(self):
        a = self.kartenstapel
        for i in range(0, len(a)-1):
            j = random.randint(i, len(a)-1)
            a[i], a[j] = a[j], a[i]


    def abheben(self):
        a = self.kartenstapel
        j = random.randint(4, len(a) - 5)
        self.kartenstapel = a[j:]+a[:j]

    def kartengeben(self):
        a = self.kartenstapel
        #reihum jeweils drei Karten an jeden Spieler
        for i in range(3):
            self.spieler1.append(a.pop(0))
        for i in range(3):
            self.spieler2.append(a.pop(0))
        for i in range(3):
            self.spieler3.append(a.pop(0))


        #zwei Karten auf den Skat
        self.skat = a[:2]
        a.pop(0)
        a.pop(0)

        for i in range(4):
            self.spieler1.append(a.pop(0))
        for i in range(4):
            self.spieler2.append(a.pop(0))
        for i in range(4):
            self.spieler3.append(a.pop(0))


        for i in range(3):
            self.spieler1.append(a.pop(0))
        for i in range(3):
            self.spieler2.append(a.pop(0))
        for i in range(3):
            self.spieler3.append(a.pop(0))



spiel = Skatspiel()
print(spiel)
print()

spiel.mischen()
print(spiel)
print()

spiel.abheben()
print(spiel)
print()

spiel.kartengeben()
print(spiel)
