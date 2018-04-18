def transponiere(a):
    b = []

    for j in range(len(a[0])):
        c = []
        for i in range(len(a)):
            c.append(a[i][j])
        b.append(c)
    return b

def zeilen_und_spalten_sortiert(a):

    for j in range(len(a[0])-1):
        for i in range(len(a)):
            if a[i][j] >= a[i][j+1]:
                return False
    a = transponiere(a)

    for j in range(len(a[0])-1):
        for i in range(len(a)):
            if a[i][j] >= a[i][j+1]:
                return False
    return True



a = [[1,2],[3,4],[5,6],[7,8]]
print(transponiere(a))
print(zeilen_und_spalten_sortiert(a))