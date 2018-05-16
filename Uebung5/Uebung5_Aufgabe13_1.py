#sauce head:

length = int(input())
b = list()

#Code:

#berechnung Binomialkoeffizienten

def binom(n, k):
    b = 1
    for i in range(k-1, -1, -1):
        b *= n-i
        b //= k-i
    return b

#erzeugen des felds:

def pascal_d(n):
    output = list()
    for zeile in range(n):
        tmp = list()
        for spalte in range(zeile+1):
            #print("zeile:", zeile, "spalte:", spalte)
            tmp.append(binom(zeile, spalte))
            #print(tmp)
        output.append(tmp)
    return output



#ausführen:

b = pascal_d(length)
#print(b)

#Sauce footer:

correct = (len(b)==length)
for i in range(len(b)):
    correct = correct and (len(b[i]) == i+1)
    for j in range(len(b[i])):
        if(j==0 or j==(len(b[i])-1)):
            correct = correct and b[i][j] == 1
        else:
            correct = (correct and (b[i][j] == b[i-1][j-1]+b[i-1][j]))

if correct:
    print("correct!")
else:
    print("not correct!")
    print("your solution:")
    for i in range(len(b)):
        print(b[i])
