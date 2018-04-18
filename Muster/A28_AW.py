def bitonisch(a):
    i = 0
    while a[i] <= a[i+1]:
        i += 1
    else:
        while a[i] >= a[i+1]:
            i+= 1
            if i == len(a) - 1:
                return True
        else:
            return False

def maxElement(a,links,rechts):
    if rechts < links:
        return False
    mitte = (links+rechts)//2

    if a[mitte]< a[mitte+1]:
        return maxElement(a,mitte+1,rechts)
    elif a[mitte] < a[mitte-1]:
        return maxElement(a,links, mitte-1)
    else:
        return a[mitte]


a = [1,2,5,7,9,2,1]
print(bitonisch(a))
print("max",maxElement(a,0,len(a)))
