#Please insert your Code here!
#####################Kopiert aus aufgabe 34 um das geschlecht abzugleichen#############
datei = open('Frauennamen.txt','r',encoding='ISO-8859-1')
satzw=set()

for line in datei:
    s=line.split()
    for i in range(len(s)):
        satzw.add(s[i])
datei.close()

datei = open('Maennernamen.txt','r',encoding='ISO-8859-1')
satzm=set()

for line in datei:
    s=line.split()
    for i in range(len(s)):
        satzm.add(s[i])

datei.close()
schnitt=set()
schnitt=satzw.intersection(satzm)
liste=list(schnitt)
liste.sort()

###############################Anfang der eigentlichen aufgabe 35###########################

male=0
female=0
erhalten={}     #wörterbuch der erhaltenen anfragen
wunsch={}       #wörterbuch der abgegebenen anfragen
satz=set()      #set zur ermittlung der gesamtuser
zahl=0          #zähler für die einträge

datei = open('Partnerboerse.txt.txt','r',encoding='ISO-8859-1')
for line in datei:
    zahl+=1
    s=line.split(' -> ')                #???bekomme bei diesem split etliche zeilenumbrüche deshalb...
    if s[1][len(s[1])-1]=='\n':         #wenn letztes zeichen zeilenumbruch ...
        s[1]=s[1][:-1]                  #lösche letztes zeichen
    if s[1] in erhalten:                #eintrag bereits im wörterbuch?
        erhalten[s[1]].append(s[0])     #dann erweitere das feld
    else:
        erhalten[s[1]]=[s[0]]           #sonst lege ein neues feld an
    if s[0] in wunsch:                  #eintrag vorhanden?
        wunsch[s[0]].append(s[1])       #feld erweitern
    else:                               #
        wunsch[s[0]]=[s[1]]             #neues feld anlegen
    satz.add(s[0])
    satz.add(s[1])
datei.close()
print("Die Partnerbörse hat ",len(satz)," User")
print("Die Datenbank hat ",zahl," einträge")
liste=list(satz)
for x in liste:         ##################
    if x in satzw:      #geschlechter ermitteln
        female += 1     #
    if x in satzm:      #
        male += 1       ############

print("Von den",len(liste), 'Usern sind,', male, 'männlich , und', female, 'weiblich ')

match=0
for k in wunsch:                ###################################
    for h in wunsch[k]:         #gegenseitige wünsche ermitteln
        if h in wunsch:         #indem die wörterbücher auf einträge
            if k in wunsch[h]:  #und gegenseitige schlüssel verglichen werden
                match+=1        ####################################

#match=match//2 beruhen x oder x//2 anfragen auf gegenseitigkeit?
print('auf gegenseitigigkeit beruhen',match,'anfragen')
hilf=0
name=''
for y in wunsch:                ###################################
    if len(wunsch[y])>hilf:     #ermitteln des kontaktfreudigsten in dem das längste feld
        hilf=len(wunsch[y])     #im wunsch-wörterbuch gesucht wird
        name=y                  ###################################
print(name,'ist am kontaktfreudigsten und hat ',hilf,' wuensche abgegeben')
print(wunsch[name])

hilf2=0
name2=''
for z in erhalten:              #####################################
    if len(erhalten[z])>hilf2:  #beliebtesten ermitteln analog zum
        hilf2=len(erhalten[z])  #kontaktfreudigsten
        name2=z                 ####################################
print(name2,' ist am beliebtesten mit ',hilf2,' anfragen')
print(erhalten[name2])

summe=0
for person in wunsch:                   # gewinn mit der gegebenen formel ermitteln
    if person in erhalten:              #nur personen in  betracht ziehen die sowohl eine anfrage erhalten als auch abgegeben haben
        summe+=len(wunsch[person])*len(erhalten[person])
print('Der Umsatz beträgt ',summe,'€')