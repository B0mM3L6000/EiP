n = int(input("Welche Zahl soll zerlegt werden?"))

p = 2

ende = False

if n == 1:
    ende = True


print("1", end='')

while ende == False:
    if (n-p) == 0:
        ende = True
        print("*",p)
        break
    if n%p == 0:
        print("*",p, end='')
        n = n//p
    else:
        p = p+1



"""
Aufgabenteil 2:

256 = 1* 2* 2* 2* 2* 2* 2* 2* 2    -> 9 Faktoren
300 = 1* 2* 2* 3* 5* 5             -> 6 Faktoren

256 besteht aus mehr Faktoren

Aufgabenteil 3:

Da der kleinste gemeinsame Teiler einer Zahl immer eine Primzahl ist und wir
jedesmal wieder vorne anfangen zu teilen je neu geupdatete Zahl n, finden wir nur
diese kleinsten gemeinsamen Teiler, also nur Primzahlen.


"""
