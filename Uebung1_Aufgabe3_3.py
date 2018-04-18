#n gesucht

import math

K = float(input("Was ist das Endkapital?"))
K0 = float(input("Was ist das Startkapital?"))
p = float(input("Was ist der Zins?"))

# log(K/K0) = log(1+p) * n
# -> log(K/K0) / log (1+p) = n

n = math.log((K/K0))/math.log((1+p))


print("Du hast über ", n ," Perioden angelegt.")