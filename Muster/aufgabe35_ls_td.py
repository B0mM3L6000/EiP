# Please insert your Code here!
def number_of_people_m_w(file):
    datei = open(file, "r", encoding='ISO-8859-1')
    frauennamen = open("Frauennamen.txt", "r", encoding='ISO-8859-1')
    maennernamen = open("Maennernamen.txt", "r", encoding='ISO-8859-1')
    temp = []
    M = []
    F = []
    N = []
    l = 0
    for line in datei:
        l += 1
        s = line.split()
        if s[0] not in temp:  # wir merken uns alle name die einen wunsch abgegeben haben
            temp.append(s[0])
        if s[2] not in temp:  # falls jemand keinen Wunsch abgegeben hat, überprüfen wir auch name2
            temp.append(s[2])
            # wir gehen die Namen durch und überprüfen, ob es ein Frauen-/Maennername ist
    for e in temp:
        if e in maennernamen and e in frauennamen:
            N.append(e)
        if e in maennernamen:
            M.append(e)
        elif e in frauennamen:
            F.append(e)
        else:
            N.append(e)
    datei.close()
    frauennamen.close()
    maennernamen.close()
    return l, len(temp), len(M), len(F), len(N)


(l, angemeldet, anzahl_m, anzahl_w, n) = number_of_people_m_w("Partnerboerse.txt")
print("Zahl der Personen, deren Geschlecht nicht zugeordnet werden kann:", n)


# wir erstellen zwei dictionaries,im erstenwerden die Wünsche jeder Person in listen gespeichert,
# falls mehrere abgegeben wurden
# im zweiten werden die Wünsche als key verwendet
def erstellen_dictionary(file):
    datei = open(file, "r", encoding='ISO-8859-1')
    name1_name2 = {}
    name2_name1 = {}
    for line in file:
        s = line.split()
        name1 = s[0]
        name2 = s[2]
        if name1 not in name1_name2:
            name1_name2[name1] = [name2]
        else:
            name1_name2[name1] += [name2]
        if name2 not in name2_name1:
            name2_name1[name2] = [name1]
        else:
            name2_name1[name2] += [name1]
    datei.close()
    return name1_name2, name2_name1


#
def Interesse(file):
    (n1_n2, n2_n1) = erstellen_dictionary(file)
    t = 0 #wir zählen die gegenseitigen Wünsche
    g = 0 #wir zählen die Anzahl der meist abgegebenen Wünsche
    for e in n1_n2.keys():  #wir gehen die Schlüssel durch und schauen wie viele Elemente
        if len(n1_n2[e]) > g:  #in der dazugehörigen Liste stehen und speichern die größe in l
            g = len(n1_n2[e])  #wenn sie länger als der vorherige ist
        #wir gehen die Elemente der Liste vom key name1 durch und nehmen jedes als key im n2_n1
        #und überprüfen ob dort name1 zu finden ist
        for i in range(len(n1_n2[e])):
            s = n1_n2[e][i]
            if e in n2_n1.keys():
                if s in n2_n1[e]:
                    t += 1
    return t//2, g, beliebteste_Person(n2_n1), mein_Gewinn(n1_n2, n2_n1)


# wir gehen alle keys im dictionary durch und merken uns jeweils die höhere anzahl an Elementen
# in der zugehörigen Liste
def beliebteste_Person(dict):
    l = 0
    for p in dict.keys():
        if len(dict[p]) > l:
            l = len(dict[p])
    return l


def mein_Gewinn(dict1, dict2):
    s = 0
    for name1 in dict1.keys():
        t = len(dict1[name1])
        if name1 in dict2:
            r = len(dict2[name1])
        else:
            r = 0
        s += t * r
    return s


(anzahl_beiseitiges_Interresse, anzahl_g_Kontaktanfragen, anzahl_beliebste_Person, mein_gewinn) = Interesse(
    "Partnerboerse.txt")

print("Anzahl der Zeilen von Partnerboerse.txt:", l)
print("Anzahl an verschiedenen Personen:", angemeldet)
print("Anzahl der Männer:", anzahl_m)
print("Anzahl der Frauen:", anzahl_w)
# Noch nicht sicher, ob 0 rauskommt bei beidseitigem Interesse
print("Anzahl der Beziehungswünsche, die auf Gegenseitigkeit beruht:", anzahl_beiseitiges_Interresse)
print("Anzahl der meisten Kontaktwünschen:", anzahl_g_Kontaktanfragen)
print("Anzahl der Kontaktwünsche auf eine Person:", anzahl_beliebste_Person)
print("Gewinn meiner Partnerbörse:", mein_gewinn, "€")