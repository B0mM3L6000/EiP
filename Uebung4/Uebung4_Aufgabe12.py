import random

# die Liste der gezogenen Lottozahlen
#picks = list()

#liste der zur auswahl stehenden zahlen (hier 1-49)
zahlen = list(range(1,50))

#anzahl der ziehungen (hier 6 aus 49)
anzahl = 6


#ziehungen: jeweils eine zahl ziehen und zu picks hinzufügen und aus zahlen entfernen um doppelte zu vermeiden
for i in range(anzahl):
    j = random.randint(0, len(zahlen)-i)
    picks.append(zahlen[j])
    zahlen.remove(zahlen[j])

#sortieren
picks.sort()






#Sauce Output:

print("#test if 6 different numbers were drawn")
if(len(set(picks)) == 6):
    print("all picks are unique")
else:
    print("at least two picks are the same")
    print("your picks:", picks)
print("#test if all picks are in range from 1 to 49")
if(all(k in range(1,50) for k in picks)):
    print("picks in valid range")
else:
    print("picks are not in valid range")
    print("your picks:", picks)
print("#test if picks are sorted")
if(sorted(picks) == picks):
    print("picks are sorted")
else:
    print("picks are not sorted!")
    print("your picks:", picks)
