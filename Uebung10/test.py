string1 = "baum haus welt"
string2 = "rot green blau"

list1 = str.split(string1)
list2 = str.split(string2)
encoding = {}
for i in range(len(list1)):
    encoding[list1[i]] = list2[i]

print(encoding)

string = "haus welt welt"


encodedstring = ""
toencode = str.split(string)
for i in range(len(toencode)):
    encodedstring += encoding[toencode[i]] + " "
print(encodedstring)

string =" blau blau blau"


decodedic = {}
for key in encoding:
    decodedic[encoding[key]] = key
print(decodedic)
decodedstring = ""
todecode = str.split(string)
for i in range(len(todecode)):
    decodedstring += decodedic[todecode[i]] + " "
print(decodedstring)
