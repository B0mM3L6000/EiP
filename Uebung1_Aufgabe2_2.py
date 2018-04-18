zahl1 = float(input("Zahl1:"))
zahl2 = float(input("Zahl2:"))
zahl3 = float(input("Zahl3:"))

print("Die Größte Zahl ist:")

if zahl1 > zahl2:
    if zahl1 > zahl3:
        print(zahl1)
    elif zahl1 < zahl3:
        print(zahl3)
    else:
        print(zahl1, "und", zahl3)
elif zahl1 < zahl2:
    if zahl2 > zahl3:
        print(zahl2)
    elif zahl2 < zahl3:
        print(zahl3)
    else:
        print(zahl2, "und", zahl3)
elif zahl1 == zahl2:
    print(zahl1, "und", zahl2)
else:
    print(zahl1, ",",zahl2,"und", zahl3)