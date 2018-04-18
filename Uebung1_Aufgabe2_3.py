zahl1 = float(input("Zahl1:"))
zahl2 = float(input("Zahl2:"))
zahl3 = float(input("Zahl3:"))

i = 0

if zahl1 == zahl2:
    if zahl2 == zahl3:
        print("1 einzigartiger Wert.")
    else:
        print("2 einzigartige Werte.")
else:
    if zahl2 == zahl3:
        print("2 einzigartige Werte.")
    elif zahl3 == zahl1:
        print("2 einzigartige Werte.")
    else:
        print("3 einzigartige Werte.")