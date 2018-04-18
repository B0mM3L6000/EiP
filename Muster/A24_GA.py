import itertools

"""
We define print function for field
We develop function, that checks if mine placement attempt has caused fail.
 For example take every number on field, and check on valid on every attempt
for solving
 take every given number and attempt to place bombs near it until it has right count
 check field
 if all right go to next number
 if all right for the last => solved
 if not => step back
"""
a = [[ 1,-1,-1,-1,-1, 3,-1],
     [-1,-1,-1,-1,-1,-1,-1],
     [-1, 1,-1,-1, 0,-1,-1],
     [-1,-1,-1, 2,-1,-1,-1],
     [-1, 3,-1,-1,-1,-1, 3],
     [-1,-1,-1,-1, 1,-1,-1],
     [-1,-1,-1, 1,-1,-1, 1]]

b = [[-1, -1, -1, -1, -1, -1, 1],
     [2, -1, -1, -1, 2, -1, -1],
     [-1, -1, 3, -1, -1, -1, 1],
     [-1, -1, 3, -1, -1, -1, -1],
     [2, -1, 1, -1, 1, 3, -1],
     [-1, 3, -1, -1, -1, -1, 1],
     [-1, -1, -1, 2, -1, -1, -1]]

c = [[-1, -1, -1, -1, 1, -1, -1],
     [-1, 3, 1, -1, -1, 3, -1],
     [2, -1, -1, 3, -1, 2, -1],
     [-1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, 3, 2, -1, -1],
     [-1, 2, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, 1]]


def print_tentaizu(a, n):
    for i in range(n+3):
        print("_", end='')
    print()
    for i in range(n):
        print("| ", end='')
        for j in range(n):
            if a[i][j] >= 0:
                print(a[i][j],end='')
            elif a[i][j] == -1:
                print('.',end='')
            elif a[i][j] == -2:
                print(' ',end='')
            else:
                print('*',end='')
        print("| ")
    for i in range(n + 3):
        print("_", end='')
    print()

def bounds(a, z, s):
    n = len(a)
    mines = 0
    possible = 0
    for i in range(-1, 2):
        if z + i < 0 or z + i > n - 1:
            continue
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if s + j < 0 or s + j > n - 1:
                continue
            if a[z + i][s + j] == -1:
                possible += 1
            if a[z + i][s + j] == -3:
                mines += 1
                possible += 1
    return (mines, possible)


def valid(a, z, s):
    for i in range(-1, 2):
        if z + i < 0 or z + i > 6:
            continue
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if s + j < 0 or s + j > 6:
                continue
            if a[z + i][s + j] < 0:
                continue
            (u, o) = bounds(a, z + i, s + j)
            if a[z + i][s + j] < u or a[z + i][s + j] > o:
                return False
    return True

def form_list(a):
    n = len(a)
    feld = []
    for i in range(n):
        for j in range(n):
            if a[i][j] >= 0:
                feld.append([a[i][j], (i, j), 0, list(itertools.combinations(range(8), a[i][j]))])

    return feld


def solve(a, k, fixed, ind):
    # print_tentaizu(a, 7)
    # if k > 10:
    #   print("Too many mines", fixed[ind][0], fixed[ind][1], fixed[ind][2])
    #    return False
    if not check_field(a, fixed):
        # print("Mines conflict", fixed[ind][0], fixed[ind][1], fixed[ind][2])
        return False
    if ind == len(fixed):
        print_tentaizu(a, 7)
        # print("End?", fixed[ind][0], fixed[ind][1], fixed[ind][2])
        return True
    info = fixed[ind][0]
    (z, s) = fixed[ind][1]
    mines = bounds(a, z, s)[0]

    if mines == info: # all mines placed, go next
        # print("Mines placed, next info", fixed[ind][0], fixed[ind][1], fixed[ind][2])
        solve(a, k, fixed, ind + 1)
    else:
        # place mines and call solve
        if z == 4:
            asd= 1
        tt = fixed[ind][2]
        # if tt < len(fixed[ind][3]):
            # print("Place mine", fixed[ind][0], fixed[ind][1], fixed[ind][2], fixed[ind][3][tt], end='')
            # for item in fixed[ind][3][tt]:
                # print(assign(item), end='')
            # print()
        if next_placement(a, info, (z,s), fixed[ind][2], fixed[ind][3]):
            # print("Good placement", fixed[ind][0], fixed[ind][1], fixed[ind][2])
            # print_tentaizu(a, 7)
            if not solve(a, k + info, fixed, ind):
                # undo_placement(a, info, (z,s), fixed[ind][2], fixed[ind][3])
                # print_tentaizu(a, 7)
                undo_placement(a,fixed,ind)
                # print_tentaizu(a, 7)
                # print("Not solved, try next one", fixed[ind][0], fixed[ind][1], fixed[ind][2])
                fixed[ind][2] += 1
                if fixed[ind][2] == len(fixed[ind][3]):
                    fixed[ind][2] = 0
                    # print("All placements failed. Go back", fixed[ind][0], fixed[ind][1], fixed[ind][2])
                    return False
                return solve(a, k, fixed, ind)
        else:
            # print("Bad placement", fixed[ind][0], fixed[ind][1], fixed[ind][2])
            fixed[ind][2] += 1
            if fixed[ind][2] == len(fixed[ind][3]):
                fixed[ind][2] = 0
                # print("All placements failed. Go back", fixed[ind][0], fixed[ind][1], fixed[ind][2])
                return False
            solve(a, k, fixed, ind)
        return False
    return False


def check_field(a, fixed):
    # print_tentaizu(a, 7)
    for item in fixed:
        info = item[0]
        (z, s) = item[1]
        mines = bounds(a, z, s)[0]
        if mines > info:
            return False
    return True


def next_placement(a, info, koord, index, feld):
    n = len(a)
    (z, s) = koord
    for item in feld[index]:
        (i, j) = assign(item)
        if s + j < 0 or s + j > n - 1 or z + i < 0 or z + i > n - 1:
            return False
        if a[z + i][s + j] > -1:
            return False

    for item in feld[index]:
        (i, j) = assign(item)
        a[z + i][s + j] = -3

    return True

def undo_placement(a, fixed, index):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == -3:
                a[i][j] = -1
    # print_tentaizu(a, 7)
    for i in range(index):
        # print("Placement", i,fixed[i][0],fixed[i][1],fixed[i][2],fixed[i][3] )
        next_placement(a, fixed[i][0],fixed[i][1],fixed[i][2],fixed[i][3] )
    return True


def assign(num):
    t = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if t == num:
                return (i,j)
            else:
                t += 1
    return (-1, -1)

to_solve = a
print_tentaizu(to_solve,7)
fixed= form_list(to_solve)
print("All possible solutions")
solve(to_solve, 0, fixed, 0)