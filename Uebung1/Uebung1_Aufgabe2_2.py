zahl1 = int(input("Zahl1:"))
zahl2 = int(input("Zahl2:"))
zahl3 = int(input("Zahl3:"))

print("Die Größte Zahl ist:")

#die einzelnen Fälle überprüfen und den entsprechenden Fall ausgeben:

if zahl1 > zahl2 and zahl1 > zahl3:
    print("Zahl1 ist am größten und hat den Wert ", zahl1)
elif zahl2 > zahl1 and zahl2 > zahl3:
    print("Zahl2 ist am größten und hat den Wert ", zahl2)
elif zahl3 > zahl1 and zahl3 > zahl2:
    print("Zahl3 ist am größten und hat den Wert ", zahl3)
elif zahl1 > zahl2 and zahl1 == zahl3:
    print("Zahl1 und Zahl3 sind am größten und haben den Wert ", zahl1)
elif zahl2 > zahl1 and zahl2 == zahl3:
    print("Zahl2 und Zahl3 sind am größten und haben den Wert ", zahl2)
elif zahl1 > zahl3 and zahl1 == zahl2:
    print("Zahl1 und Zahl2 sind am größten und haben den Wert ", zahl1)
elif zahl1 == zahl2 and zahl1 == zahl3:
    print("Alle drei Zahlen haben den selben Wert: ", zahl1)
