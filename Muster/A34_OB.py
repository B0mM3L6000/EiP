def read_file_names(namen):
    frau = False
    names_m = []
    names_w = []
    datei = open(namen,'r')
    for line in datei:
        s = line.split("\n")
        if s[0] == "Frauennamen":
            frau = True
            continue
        if frau:
            names_w.append(s[0])
        else:
            names_m.append(s[0])
    return (names_m,names_w)

def delete_duplicate_names(names):
    unique = []
    [unique.append(item) for item in names if item not in unique]
    return unique

def delete_duplicate_names_sorted(names):
    for i in range (len(names)-1):
        add = 1
        while True:
            if names[i]!= names[i+add] or i+add == len(names):
                break
            else:
                names[i+add] = "."
                add += 1
    names_shorted = []
    for i in range(len(names)):
        if names[i] != ".":
            names_shorted.append(names[i])
    return names_shorted

def delete_duplicate_names_set(array):
    temp = set(array)
    return temp

def write_all_name_in_file(names,datei):
    f = open(datei,'w')
    for i in names[0]:
        if i in names[1]:
            f.write(str(i)+ "\n")
    f.close()