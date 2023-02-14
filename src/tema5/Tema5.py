# Functii

# 1. Funcție care să calculeze și să returneze suma a două numere

def sumaNumerelor(a, b):
    suma = a + b
    return suma


a = int(input('a = '))
b = int(input('b = '))
print(f'Suma numerelor este {sumaNumerelor(a, b)}')


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
def is_par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False


raspuns = is_par(7)
print(raspuns)

# 3. Funcție care returnează numărul total de caractere din numele tău complet
def name(nume, prenume):
    lungime_nume = len(nume+prenume)
    return lungime_nume
nume = input('nume:')
prenume = input('prenume:')
print('Nr total de caractere:', name(nume, prenume))

# 4. Funcție care returnează aria dreptunghiului
def aria(L, l):
    formula = L * l
    return formula
L = float(input('Lungimea dreptunghiului este:'))
l = float(input('Latimea dreptunghiului este:'))
print('Aria dreptunghiului este', aria(L, l))

# 5. Funcție care returnează aria cercului
def aria_cercului(raza):
    pi = 3.14
    form_arie = raza ** 2 * pi
    return form_arie
raza = float(input('raza = '))
print('Raza cercului este', aria_cercului(raza))

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
def caractere(string):
    if litere in string:
        return True
    else:
        return False
litere = input('Litera pe care doriti sa o verificati:')
string = input('Propozitia:')
print(caractere(string))

''' 7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y'''
def caractere(test):
    k = {'Litere_mari':0, 'Litere_mici':0}
    for i in test:
        if i.isupper():
            k['Litere_mari'] += 1
        elif i.islower():
            k['Litere_mici'] += 1
        else:
            pass
    print('Prop este:', test)
    print('Nr lit mari:', k['Litere_mari'])
    print('Nr lit mici:', k['Litere_mici'])
caractere('Dan merge in PARK')

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive
def creare_lista():
    lista = [1, 2, -7, 8, -5, -3, 0.5, 12.3, 5, -5.2]
    nr_nat = []
    if lista >= 0:
        return nr_nat.append()
    else:
        return 'nu sunt nr naturale in lista'


# 10.
def set_nou(nr, set):
    if nr in set:
        print('nr deja exista')
        return False
    else:
        set.add(nr)
        print('adauga nr in set')
        return True
set = {2, 6, 8}
print(set_nou(13, set))