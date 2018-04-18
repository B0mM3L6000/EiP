def istPalindrom(z):
    for i in range(len(z)//2):
        if z[i] != z[len(z)-i-1]:
            return False
    return True


def istPalindromRekursiv(z):
    if z == '':
        return True
    if z[0] != z[len(z)-1]:
        return False
    print(z[1:len(z)-1])
    return istPalindromRekursiv(z[1:len(z)-1])


z = 'reliefpfeiler'
print(istPalindrom(z))
print()
print(istPalindromRekursiv(z))
