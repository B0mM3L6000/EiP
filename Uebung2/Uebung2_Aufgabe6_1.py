n = int(input("Welcher Wert für n?"))

i = 1
zeilenbreite = n + (n-1)

for _ in range(n):
    print(zeilenbreite*"0")
