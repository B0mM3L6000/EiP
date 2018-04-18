# Wir ueberpruefen, ob die Dame in der k-ten Spalte von einer der Damen
# in Spalte 0 bis Spalte k-1 geschlagen werden kann.
def valid(a,k):
    for i in range(0,k):
        # Horizontale
        if a[i] == a[k]:
            return False
        # steigende Diagonale
        if a[k]-a[i] == k-i:
            return False
        # fallende Diagonale
        if a[k]-a[i] == i-k:
            return False

    return True


# Die rekursive Funktion solve implementiert eine Backtracking-Strategie
# zur Loesung des n-Damen-Problems. Im Feld a ist eine Teilloesung gespeichert,
# die zu einer Gesamtloesung ausgebaut werden soll. Der Parameter k gibt die
# Spalte an, in der die naechste Dame platziert werden soll. Die Funktion
# liefert den Wert true zurueck, wenn die vorgegebene Teilloesung (also die
# Platzierung der Damen 0 bis k-1) eine valide Restloesung (also die Platzierung
# der Damen von k bis n-1) erlaubt.

def solve(a,k):
    n = len(a)
    # Das Rekursionsende ist erreicht, wenn alle Damen von Spalte 0 bis n-1
    # platziert wurden, d.h. k hat den Wert n erreicht.
    if k == n:
        global anzahl
        anzahl += 1
        return True
    # Wir versuchen die aktuelle Teilloesung zu erweitern, indem wir in der
    # k-ten Spalte eine Dame auf jede valide Position platzieren und durch
    # einen rekursiven Aufruf der solve-Funktion ueberpruefen, ob diese so
    # erweiterte Teilloesung zu einer Gesamtloesung vervollstaendigt werden kann.
    for i in range(0,n):
        # Wir setzen die Dame in Spalte k in die i-te Zeile.
        a[k] = i
        # Wenn dadurch keine valide Konfiguration entsteht, gehen wir zur naechsten
        # moeglichen Postition ueber.
        if  not valid(a,k):
            continue
        # Wir ueberpruefen, ob sich das Restproblem (d.h. die Platzierung der Damen
        # k+1 bis n-1) loesen laesst. Falls ja, haben wir eine Gesamtloesung gefunden
        # und geben true zurueck. Falls nein, untersuchen wir die naechste Position
        # in der k-ten Spalte.
        if solve(a,k+1):
            continue
            return True

    # Alle Positionen der k-ten Dame in der k-ten Spalte haben dazu gefuehrt, dass
    # ein unloesbares Restproblem entstanden ist. Wir befinden uns in einer "Sackgasse"
    # und melden an die aufrufende Funktion zurueck, dass die im a-Feld uebergebene
    # Teilloesung sich nicht vervollstaendigen laesst. Es liegt in der Verantwortung
    # der aufrufenden Funktion, alternative Teilloesungen zu generieren, die hoffentlich
    # irgendwann rekursiv vervollstaendigt werden koennen.
    return False