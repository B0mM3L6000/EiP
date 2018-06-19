import random

class Konto:
    def __init__(self, geld, inhaber, nummer):
        self.Kontostand = geld
        self.Kontoinhaber = inhaber
        self.Kontonummer = nummer

    def einzahlen(self, betrag):
        if betrag <= 0:
            return Konto(self.Kontostand, self.Kontoinhaber, self.Kontonummer)
        else:
            self.Kontostand = self.Kontostand + betrag
            return Konto(self.Kontostand, self.Kontoinhaber, self.Kontonummer)

    def abheben(self, betrag):
        if betrag > self.Kontostand and betrag < 0:
            return Konto(self.Kontostand, self.Kontoinhaber, self.Kontonummer)
        else:
            self.Kontostand = self.Kontostand - betrag
            return Konto(self.Kontostand, self.Kontoinhaber, self.Kontonummer)

    def ueberweisen(self, zielKonto, betrag):
        if betrag < 0:
            return Konto(self.Kontostand, self.Kontoinhaber, self.Kontonummer), Konto(zielKonto.Kontostand, zielKonto.Kontoinhaber, zielKonto.Kontonummer)
        else:
            if self.Kontostand < betrag:
                return Konto(self.Kontostand, self.Kontoinhaber, self.Kontonummer), Konto(zielKonto.Kontostand,
                                                                                          zielKonto.Kontoinhaber,
                                                                                          zielKonto.Kontonummer)
            else:
                self.Kontostand = self.Kontostand - betrag
                zielKonto.Kontostand = zielKonto.Kontostand + betrag
                return Konto(self.Kontostand, self.Kontoinhaber, self.Kontonummer), Konto(zielKonto.Kontostand, zielKonto.Kontoinhaber, zielKonto.Kontonummer)

    def __str__(self):
        printing = "Konto: "
        printing += str(self.Kontonummer) + " - Inhaber: " + str(self.Kontoinhaber) + " - Kontostand: " + str(self.Kontostand)
        return printing
        #return str((-Konto: self.Kontonummer - Inhaber: ',self.Kontoinhaber,' - Kontostand: ',self.Kontostand))



Konto1 = Konto(0, "Martin", 1)
Konto2 = Konto(-20, "Henry", 2)

Konto1.einzahlen(100)
Konto1.ueberweisen(Konto2,37)
Konto2.abheben(40)
randomnumber = random.randint(1,50)
Konto2.einzahlen(randomnumber)
abhebesumme = Konto2.Kontostand
Konto2.abheben(abhebesumme)

print(Konto1)
print(Konto2)

###################
"""
Konto1 = Konto(5, "Max", 1)
Konto2 = Konto(-9, "Maria", 2)

print(Konto1)
print(Konto2)

Konto1.einzahlen(5)

print(Konto1)
print(Konto2)

Konto2.abheben(17)

print(Konto1)
print(Konto2)

Konto2.ueberweisen(Konto1, 4)

print(Konto1)
print(Konto2)

Konto1.abheben(3)

print(Konto1)
print(Konto2)

Konto1.ueberweisen(Konto2, 7)

print(Konto1)
print(Konto2)

Konto1.ueberweisen(Konto2,-3)

print(Konto1)
print(Konto2)

Konto1.abheben(-3)
"""
