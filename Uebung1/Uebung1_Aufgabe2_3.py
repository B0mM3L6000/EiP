zahl1 = int(input("Zahl1:"))
zahl2 = int(input("Zahl2:"))
zahl3 = int(input("Zahl3:"))


#1)   zunächst eine Verzweigung ob Zahl1 = zahl2 ist oder nicht.
#1.1) Falls dies der Fall ist überprüfen ob auch zahl3 gleich ist oder nicht
#     und dann entsprechenden Fall ausgeben.
#2)   Falls 1) nicht erfüllt ist wird else ausgeführt.
#2.2) Überprüfung ob zahl3 entweder gleich zahl1 oder 2 ist und gegebenfalls
#     ausgeben. Sollte dies nicht der Fall sein, so sind alle 3 Zahlen
#     unterschiedlich und dies wird ausgegeben.

if zahl1 == zahl2:
    if zahl2 == zahl3:
        print("1 unterschiedlicher Wert.")
    else:
        print("2 unterschiedliche Werte.")
else:
    if zahl2 == zahl3:
        print("2 unterschiedliche Werte.")
    elif zahl3 == zahl1:
        print("2 unterschiedliche Werte.")
    else:
        print("3 unterschiedliche Werte.")
