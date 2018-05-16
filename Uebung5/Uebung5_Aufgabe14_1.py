#sauce head:

import random
# Die sortierte Liste
random.seed()
a = [random.randint(1,1000) for i in range(5000)]
a.sort()

#Die zu suchende Zahl
x = int(input())

#Rueckgabe bei Erfolg
found = False



#CODE:









#sauce footer:

if found == (x in a):
    print("correct!")
else:
    print("not correct!")
