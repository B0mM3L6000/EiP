def zulaessig(stellung):
    n = len(stellung)
    for i in range(n-1):
        if stellung[i] == stellung[n-1]:
            return False
        if abs(stellung[i]-stellung[n-1]) == n-1-i:
            return False
    return True

def vervollstaendige(stellung, count = 0):
    global counter
    counter = count
    #solutions = solutions2

    if len(stellung) == n:
        if zulaessig(stellung):
            #print("zulaessig gefunden")
            counter +=1
            #print (counter)
            #solutions = addsolution(stellung, solutions)


    for y in range(n):
        stellung.append(y)
        if zulaessig(stellung):
           vervollstaendige(stellung, counter)
        stellung.pop()
    #print(stellung)
    if stellung == []:
        return counter
"""
def addsolution(stellung, solutions):
    solutions.append(stellung)
    return solutions
    #print("test")
"""
#Test fuer das 8-Damen Problem
#counter = 0
stellung = []
n = 12
print(vervollstaendige(stellung))
#print(solutions)
#print(len(solutions))
"""
#Test fuer das 10-Damen Problem
stellung = []
n = 10
print(vervollstaendige(stellung))
#print(solutions)
#print(len(solutions))
"""
