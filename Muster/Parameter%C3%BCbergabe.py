# Von Christian Stricker

def f(x,y):
    x.append(y[0])
    y.append(x[0])
    y = [x[1]]
    y.append(x[2])
    return y

a = [1,2,3]
b = [4,5,6]
"""
a -> <42> -> [1,2,3]    Variable a wird neu angelegt(z.b. in Speicheradresse 42)
b -> <44> -> [4,5,6]    Variable b wird neu angelegt(z.b. in Speicheradresse 44)

Bei Funktionsaufruf f(x,y)
    a, x -> <42> -> [1,2,3]
    b, y -> <44> -> [4,5,6]

    Nach x.append(y[0]) und y.append(x[0]):
        a, x -> <42> -> [1,2,3,4]   Variable x/a wird verändert
        b, y -> <44> -> [4,5,6,1]   Variable y/b wird verändert

    Bei y = [x[1]]
        a, x -> <42> -> [1,2,3,4]   Variable x/a wird verändert
        b    -> <44> -> [4,5,6,1]   Variable y/b wird verändert
        y    -> <99> -> [2,3]       Variable wird "neu angelegt"
"""



print(a)
print(b)
print(f(a,b))
print(a)
print(b)





