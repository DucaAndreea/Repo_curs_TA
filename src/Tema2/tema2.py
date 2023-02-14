# 1.
# Un if else functioneaza de sus in jos si se utilizeaza atunci cand exista 2 sau mai multe posibilitati (Andreea daca(if) are peste 18 ani este majora, daca nu (else), este minora)
from random import randint
from re import U

# 2.
x = 3
if x > 0:
    print('Numarul este natural')
else:
    print('Numarul nu este natural!')

# x = int(input('Numar:'))
# if x > 0:
#     print('Numarul este natural')
# else:
#     print('Numarul nu este natural!')

# 3.
x = 12
if x > 0:
    print('Numarul este pozitiv!')
elif x == 0:
    print('Numarul este neutru!')
else:
    print('Numarul este negativ')

# 4.
if x >= -2 and x <= 13:
    print('Face parte din interval')
else:
    print('Nu face parte din interval')

# 5.
y = 4
diferenta = abs(x - y) - 1
if diferenta < 5:
    print('Dif mai mare de  5')
else:
    print('Dif mai mica 5')

# 6.
numere = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
if x != numere:
    print('x nu este in liste de numere')
else:
    print('x face parte din lista de numere')

# 7.
d = 3
f = 3
if d == f:
    print('d si f sunt egale')
    if d > f:
        print(d)
    else:
        print(f)
else:
    print('nu sunt egale')

# # 8.
a = 3
b = 3
c = 2

if (a == b or a == c or b == c) and (a != b or a != c or b != c):
     print('Tringhiul este isoscel')
elif a == b == c:
     print('Triunghiul este echilateral')
else:
     print('Triunghiul este oarecare')

# 9.
l= str(input('Litera:'))
vocale = [a or e or i or o or u or A or E or I or U or O]
if l != vocale:
    print(f'Litera {l} este vocala')
else:
     print(f'Litera {l} este consoana')

# 10.
nota = float(input('nota:'))
if nota > 10:
    print('Nota nu exista')
elif nota >= 9:
    print('Felicitari! Aveti nota A')
elif nota >= 8:
    print('Aveti nota B')
elif nota >= 7:
    print('Aveti nota C')
elif nota >= 6:
    print('Aveti nota D')
elif nota >= 5:
    print('Aveti nota E')
else:
    if nota < 0:
        print('Aceasta nota nu exista')
    else:
        print('Aveti F')