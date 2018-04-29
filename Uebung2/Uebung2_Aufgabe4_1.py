from math import sqrt

#gesucht alle Primzahlpaare zwischen 10101 und 10901

p = 10101 
# ab welcher Zahl soll geprüft werden?

ende = 10901 
# bis welche Zahl soll geprüft werden?

while p <= (ende-2): 
    # ende-2, damit 10901 letztmögliches Teil eines Primzahlzwillings ist.
    
    teiler = 2
    while teiler <= int(sqrt(p)):
        if p % teiler == 0:
            break 
            # p ist keine Primzahl.
            # Sprung auf Zeile 38.
        else:
            teiler += 1  
            # Prüfe, ob p durch nächsten Teiler teiler+1 ohne Rest dividierbar ist.
    else: 
        # wird nur ausgeführt, wenn die while-Schleife durchgelaufen ist.
        # p ist Primzahl, da nicht durch Teiler 2 < sqrt(p) ohne Rest dividerbar.
        # Prüfe, ob auch p+2 Primzahl ist:
        teiler_2 = 2
        while teiler_2 <= int(sqrt(p+2)):
            if (p+2) % teiler_2 == 0:
                break 
                # p ist zwar Primzahl, p+2 aber nicht. Keine Primzahlpaarbildung möglich.
            else:
                teiler_2 += 1
        else:
            # p+2 ist eine Primzahl und somit wurde eine Primzahlpaar gefunden.
            # Ausgabe (p, p+2 )
            print(p,"und",(p+2))
    p = p + 1
