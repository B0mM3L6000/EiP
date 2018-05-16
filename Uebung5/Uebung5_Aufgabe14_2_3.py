#sauce head:

import random
# Die sortierte Liste
random.seed()
a = [random.randint(1,1000) for i in range(50)]
a.sort()

#Die zu suchende Range
unten = int(input())
oben = int(input())

#Rueckgabe der Range
numElements = 0



#CODE:






#sauce footer:

if numElements == sum([1 for x in a if (x>=unten and x<=oben) ]):
    print("correct!")
else:
    print("not correct!")
    print("correct answer", sum([1 for x in a if (x>=unten and x<=oben) ]))
    print(a)
