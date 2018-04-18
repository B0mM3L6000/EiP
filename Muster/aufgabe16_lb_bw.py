def spur(M): #Summe der Diagonalen
    spur = 0 #"Zählvariable"
    for i in range(len(M)): #wir schauen uns die Matrix an
        spur += M[i][i] #und iterieren über die Diagonale
    return spur

def spaltensummennorm(M): #wir suchen die größte Summe in den Spalten
    maxsumme = 0 #Zählvariable
    for i in range (len(M)):
        summe = 0 #zwischenspeicher
        for j in range (len(M[i])):
            summe += abs(M[j][i]) # sauce wollte den absoluten Wert (der betrag von -30 > 19)
        if summe > maxsumme: #abgleich - ist die gefundene Summe größer als die vorige
            maxsumme = summe #wird getauscht
    return maxsumme


def transponiere(M):
    nm = [x[:]for x in M] #eine Kopie der Matrix wird angefertigt
    for i in range (len(nm)): #wir bewegen uns in der Kopie
        for j in range (i, len(nm)): #so wird nach und nach jedes Element durchgegangen
            nm[i][j], nm [j][i] = nm [j][i], nm [i][j] #die vertauschung findet statt
    return nm



def is_schiefsymmetrisch(M):
    c = [x[:]for x in M] #Kopie der Matrix M
    for i in range (len(c)):
        for j in range (len(c)):
            c [i][j] = - c[i][j] #verändere c so, dass sich die Vorzeichen tauschen
    if transponiere(c) == M: # Abgleich - ist die transpornierte c-Matrix die gleiche wie 
        return True #die Urpsprungsmatrix M?
    else:
        return False
