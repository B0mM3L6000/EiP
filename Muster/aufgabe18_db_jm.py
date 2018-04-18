import random


def generiere_labyrinth(m, n):
    lab = [['.' for x in range(n)] for y in range(m)]

    for y in range(0, m):
        for x in range(0, n):
            if y == 0 or y == m - 1 or y == m // 2 or x == 0 or x == n - 1:
                lab[y][x] = '#'
            elif random.random() < 0.45:
                lab[y][x] = '#'
            else:
                lab[y][x] = ' '

    lab[0][n // 2] = 'S'
    lab[1][n // 2] = ' '
    lab[m - 2][n // 2] = ' '
    lab[m - 1][n // 2] = 'Z'
    lab[m // 2][4] = ' '
    lab[m // 2][n - 4] = ' '

    return lab


def print_labyrinth(lab):
    for y in range(len(lab)):
        for x in range(len(lab[y])):
            print(lab[y][x], end='')
        print()


m = 20
n = 40
start = (0, n // 2)
ziel = (m - 1, n // 2)

lab = generiere_labyrinth(m, n)



Q=[(0,20)]
besucht=[[False for x in range(n)]for y in range (m)]
vorgaenger=[[(0,0)for x in range(n)]for y in range (m)]
dist=[[0 for x in range(n)]for y in range(m)]

besucht[0][20]=True

while len(Q)>0:
    u=Q.pop(0)

    vy=u[0]+1
    vx=u[1]
    if lab[vy][vx] != "#" and vy<=m-1:
        if  besucht[vy][vx]==False:
            Q.append((vy,vx))
            besucht[vy][vx]=True
            dist[vy][vx]=dist [u[0]][u[1]]+1
            vorgaenger[vy][vx]=(u[0],u[1])
            

    vy=u[0]-1
    vx=u[1]
    if lab[vy][vx] != "#" and vy>=0:
        if  besucht[vy][vx]==False:
            Q.append((vy,vx))
            besucht[vy][vx]=True
            dist[vy][vx]=dist [u[0]][u[1]]+1
            vorgaenger[vy][vx]=(u[0],u[1])
            

    vy=u[0]
    vx=u[1]+1
    if lab[vy][vx] != "#" and vx<=n-1:
        if  besucht[vy][vx]==False:
            Q.append((vy,vx))
            besucht[vy][vx]=True
            dist[vy][vx]=dist [u[0]][u[1]]+1
            vorgaenger[vy][vx]=(u[0],u[1])
            

    vy=u[0]
    vx=u[1]-1
    if lab[vy][vx] != "#" and vx>=0:
        if  besucht[vy][vx]==False:
            Q.append((vy,vx))
            besucht[vy][vx]=True
            dist[vy][vx]=dist [u[0]][u[1]]+1
            vorgaenger[vy][vx]=(u[0],u[1])
            

print_labyrinth(lab)