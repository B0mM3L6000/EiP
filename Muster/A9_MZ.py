#Aufgabenteil 1
for a in range(1,300):
    for b in range(a+1,300):
        for c in range(b+1,300):
            a2 = a**2
            b2 = b**2
            c2 = c**2
            if c2 == a2 + b2:
                print(a, b, c)


#Aufgabenteil 2
n = 0
for a in range(1,300):
    for b in range(a+1,300):
        A = a
        B = b
        while B>0:
            r = A % B
            A = B
            B = r
        if A == 1:
            for c in range(b+1,300):
                A = a
                C = c
                while C>0:
                    r = A % C
                    A = C
                    C = r
                if A == 1:
                    B = b
                    C = c
                    while C>0:
                        r = B % C
                        B = C
                        C = r
                    if B == 1:
                        a2 = a ** 2
                        b2 = b**2
                        c2 = c**2
                        if (c2 == a2 + b2):
                            n += 1
                            #print(n,":", a, b, c)
print(n)