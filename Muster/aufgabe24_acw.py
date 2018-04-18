from copy import deepcopy

# Definition des Feldes
zeilen = 7
spalten = 7
feld = [[-1 for y in range(spalten)] for x in range(zeilen)]
bomben = [[0 for y in range(spalten)] for x in range(zeilen)]

raetsel1 = deepcopy(feld)
raetsel2 = deepcopy(feld)

# Definition des ersten Rätselfeldes
raetsel1[0][6] = 1
raetsel1[1][0] = 2
raetsel1[1][4] = 2
raetsel1[2][2] = 3
raetsel1[2][6] = 1
raetsel1[3][2] = 3
raetsel1[4][0] = 2
raetsel1[4][2] = 1
raetsel1[4][4] = 1
raetsel1[4][5] = 3
raetsel1[5][1] = 3
raetsel1[5][6] = 1
raetsel1[6][3] = 2


feld = [[-1, -1, -1, -1, -1, -1,  1],
        [ 2, -1, -1, -1,  2, -1, -1],
        [-1, -1,  3, -1, -1, -1,  1],
        [-1, -1,  3, -1, -1, -1, -1],
        [ 2, -1,  1, -1,  1,  3, -1],
        [-1,  3, -1, -1, -1, -1,  1],
        [-1, -1, -1,  2, -1, -1, -1]]

def free_pos(feld):
    for x in range(0, 7):
        for y in range(0, 7):
            if feld[x][y] == -1:
                return (x, y)
    return (-1, -1)


def loese_raetsel(feld, k):
    if k > 10:
        return False

    (i, j) = free_pos(feld)

    if i < 0:
        return True

    feld[i][j] = "B"
    if valid(feld, i, j):
        if loese_raetsel(feld, k + 1):
            return True

    feld[i][j] = 0
    if valid(feld, i, j):
        if loese_raetsel(feld, k):
            return True
    feld[i][j] = -1
    return False


def valid(feld, zeile, spalte):
    for horizontal in [-1, 0, 1]:
        for vertikal in [-1, 0, 1]:
            tmp_zeile = zeile + vertikal
            tmp_spalte = spalte + horizontal
            if 0 <= tmp_zeile < 7 and 0 <= tmp_spalte < 7 and feld[tmp_zeile][tmp_spalte] not in ["B", -1, 0]:
                if feld[tmp_zeile][tmp_spalte] < count_bombs(feld, tmp_zeile, tmp_spalte):
                    return False
                if count_free(feld, tmp_zeile, tmp_spalte) == 0 and feld[tmp_zeile][tmp_spalte] != count_bombs(feld, tmp_zeile, tmp_spalte):
                    return False
    return True


def count_bombs(feld, zeile, spalte):
    counter = 0
    for horizontal in [-1, 0, 1]:
        for vertikal in [-1, 0, 1]:
            tmp_zeile = zeile + vertikal
            tmp_spalte = spalte + horizontal
            if 0 <= tmp_zeile < 7 and 0 <= tmp_spalte < 7 and feld[tmp_zeile][tmp_spalte] == "B":
                counter += 1
    return counter


def count_free(feld, zeile, spalte):
    counter = 0
    for horizontal in [-1, 0, 1]:
        for vertikal in [-1, 0, 1]:
            tmp_zeile = zeile + vertikal
            tmp_spalte = spalte + horizontal
            if 0 <= tmp_zeile < 7 and 0 <= tmp_spalte < 7:
                if feld[tmp_zeile][tmp_spalte] == -1:
                    counter += 1
    return counter

f = raetsel1
print(loese_raetsel(feld, 0))

for i in range(7):
    for j in range(7):
        if feld[i][j] == 0:
            print("*", ' ', end='')
        else:
            print(feld[i][j], ' ', end='')
    print()
