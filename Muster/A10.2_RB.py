l = 0
r =len(a)
x =int(input(""))
y =int(input(""))
mitte=0
while l<=r :    #Feldposition der Untergrenze bestimmen
    mitte=(l+r)//2
    if a[mitte]==x :
        untergrenze=mitte
        break
    elif a[mitte]>x:
        r =mitte-1
    else:
        l=mitte+1
if a[mitte]!=x:     #falls Wert nicht vorkommt
    untergrenze=mitte+1
l = 0
r =len(a)
while l<=r :    #Feldposition der Obergrenze bestimmen
    mitte=(l+r)//2
    if a[mitte]==y :
        obergrenze = mitte
        break
    elif a[mitte]>y:
        r =mitte-1
    else:
        l=mitte+1
if a[mitte]!=y:
    obergrenze=mitte-1
j=0
for i in range(untergrenze,obergrenze+1):   #Ausgabe der Anzahl der Feldpositionen
    j+=1
print(j)