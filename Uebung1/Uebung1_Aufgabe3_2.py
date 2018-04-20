#K0 = Startkapital
#p = Zins
#n = Perioden
#K = Endkapital


K0 = float(input("Wieviel Startkapital hast du?"))
p = float(input("Wie hoch ist der Zins?"))
n = float(input("wieviele Perioden legst du an?"))

#berechnung K

K = (K0*(1+p)**n)

print("Das Endkapital nach ", n, " Perioden beträgt: ",K)
