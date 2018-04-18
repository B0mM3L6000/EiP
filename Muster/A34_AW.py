maenner = open('Maennernamen.txt','r',encoding='ISO 8859 1')
frauen = open('Frauennamen.txt','r',encoding='ISO 8859 1')


m_namen = []
for name in open('Maennernamen.txt','r',encoding='ISO 8859 1'):
    name = name.strip()
    if name not in m_namen:
        m_namen.append(name)

print(len(m_namen))


m_namen = []
for name in open('Maennernamen.txt','r',encoding='ISO 8859 1'):
    name = name.strip()
    m_namen.append(name)

m_namen.sort()
anz_namen = 1
for i in range(1,len(m_namen)):
    if m_namen[i-1] != m_namen[i]:
        anz_namen += 1
print(anz_namen)





#Anzahl Männernamen
m_namen = set()
for name in open('Maennernamen.txt','r',encoding='ISO 8859 1'):
    name = name.strip()
    m_namen.add(name)

print(len(m_namen))

#Anzahl Frauennamen
f_namen = set()
for name in frauen:
    name = name.strip()
    f_namen.add(name)

print(len(f_namen))
