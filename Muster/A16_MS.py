def spur(Mat):
    Summe = 0
    for i in range (len(Mat)):
        Summe += Mat[i][i]
    return Summe

def spaltensummennorm(Mat):
    Maximum = 0
    for i in range (len(Mat)):
        Summe = 0
        for j in range (len(Mat)):
            Summe += abs(Mat[j][i])
        if Maximum < Summe:
            Maximum = Summe
    return Maximum
    
def transponiere(Mat):
    n = len(Mat)
    Neu = [[0 for i in range(n)] for j in range(n)]
    for i in range (n):
        for j in range (n):
            Neu[i][j] = Mat[j][i]
    return Neu

def is_schiefsymmetrisch(Mat):
    TransMat = transponiere(Mat)
    for i in range (len(Mat)):
        for j in range (len(Mat)):
            if  Mat[i][j] != -TransMat[i][j]:
                return False
    return True