#K  Kapital
#p  Zinssatz
#Z  Zinsen

#Programmablauf und Symbole

#   Start (kreis/Elipse) -> Eingabe K durch Nutzer (Parallalelogramm) -> p ist gesetzt auf 0.02 (Rechteck)
#   -> Z = K*p (Rechteck) -> Aushabe Z (Parallelogramm) -> Ende (Kreis/Elipse)

#Programm:

#Eingabe K:

K = input("Wieviel Kapital hast du?")

#Setzung Zinssatz:

p = 0.02

#Berechnung:

Z = int(K)*p

#Ausgabe:

print("Deine Zinsen nach einer Periode sind "+str(Z)+" €")