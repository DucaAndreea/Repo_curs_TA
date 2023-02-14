# Tema 3
# 1.
from typing import Dict

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)  # am afisat lista

print(note_muzicale[0], note_muzicale[-1])  # afisare primul si ultimul elem din lista
print(note_muzicale[len(note_muzicale) - 2])  # afisare penultimul element
# note_muzicale.reverse()  # lista de la dreapta la stanga
print(note_muzicale)

print(note_muzicale[0:4])
print(note_muzicale[4::])

x = note_muzicale[0:4]
print(x)
y = note_muzicale[4::]
print(y)
lista = x + y
print(lista)

# 2. De cate ori apare 'do' in lista? => functia (lista).count
print(note_muzicale.count("do"))  # 2

# 3.
a = [3, 1, 0, 2]
print(a * 2)  # am dublat elementele listei a

b = [6, 5, 4]
c = a + b
print(c)  # am unit lista a si b intr-una singura

a.extend(b)
print(a)  # lista a am extins-o cu lista b

# 4.
c.sort()
print(c)  # am sortat crescator lista c
del (c[0])
print(c)  # am sters elem 0

# 5.
c = a + b
if c != 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')
# 6.
c.clear()
print(c)  # am golit lista c

# 8.
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1)
print(len(dict1))
elevi: dict[str, int] = {
    "Ana": 8,
    "Gigel": 10,
    "Dorel": 5
}
print(elevi)
print(elevi["Ana"], dict1["Dorel"])
print(f'Ana a luat nota {8}')

# 10.
elevi["Dorel"] = 6  # modificare nota lui Dorel
print(elevi)  #

# 11.
del elevi["Dorel"]  # am sters elevul Dorel din dict
print(elevi)
elevi['Ionica'] = 9  # am adaugat elevul Ionica cu nota 9
print(elevi)

# 12.
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print(zile_sapt)
print(weekend)

zile_sapt.add('luni')
print(zile_sapt)  # elementele sunt unice
zile_sapt.add('7')
print(zile_sapt)

if 'sambata' and 'duminica' in zile_sapt:
    print('Weekend este un subset al zilelor din sapt')
else:
    print("Weekend nu este un subset al zilelor din sapt")

print(zile_sapt & weekend)  # intersectia
print(zile_sapt | weekend)  # reuniune
print(zile_sapt - weekend)  # diferenta dintre zile_sapt si weekend
print(weekend - zile_sapt)
print(zile_sapt ^ weekend) # diferenta simetrica

# Operatorii: "|" (reuniunea), "&" (intersectia), "-" (diferenta), "^" (dif simetrica)

print(zile_sapt.union(weekend)) # unirea setului zile_sapt cu weekend
print(zile_sapt.difference(weekend))
print(zile_sapt.intersection(weekend))

