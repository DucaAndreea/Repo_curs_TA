''' FUNCTIA
= este o zona de cod cu o mica logica proprie, care poate fi folosita/refolosita (apelata) de oricate ori avem nevoie
- asta e si utilitatea ei principala: ajuta sa aliminam copy-paste
- Write once, use n times
'''
print('Functia:')


def print_hi():
    print('Hi!')


print_hi()
''' PARAMETRU
= datele de intrare (input) intr-o functie
- uneori functia are nevoie de niste date ca sa poata functiona
- o functie poate sa aiba oricati parametri
- parametrii sunt optionali
- practic sunt niste variabile declarate, dar neinitializate; ele vor fi initializate la apelarea functiei
- parametrii ce se gasesc in antetul functiei se numesc PARAMETRII FORMALI
- parametrii ce se utilizeaza la apel se numesc PARAMETRII EFECTIVI (argumente)
'''
print('Functia cu parametru:')


def print_hi(user):
    print(f'Hi {user}!')


print_hi('Andreea Duca')
print_hi('Mihai Osan')

'''RETURN
- se foloseste cand functia ne si expune un raspuns (output)
- acest raspuns se poate salva in variabile
- return e optional
- se poate returna orice tip de date cunoscut
- in general, return e ultimul lucru in functie, deoarece aici se iese din functie
- in general, avem UN SINGUR return (exceptie - cand folosim if else, atunci putem avea mai multe)
'''
print('Functia cu return:')


def is_natural(numar):
    if numar >= 0:
        return 'numarul este natural'
    else:
        return 'numarul nu este natural'


raspuns = is_natural(21)
print(raspuns)  # => numarul este natural

"""print('--------------------')
n = int(input('n = '))


def subp(x):
    s = 0
    for i in range(x):
        s += 1 / (i + 1)
    return s


print(subp(n))"""

'''
- antetul functiei este: "def subp(x):", iar corpul ei, instructiunea compusa subordonata (Setul de instr INDENTATE)
- Functia (subprogramul) se numeste "subp"
-fct are un PARAMETRU numit x. Rolul sau este import deoarece precizeaza PT CE VALOARE TREBUIE CALCULATA EXPRESIA
-fct are VARIABILE PROPRII - adica definite/declarate in interiorul ei (s si i - variab locale) 
'''

"""
# functia care creaza o lista
def creare_lista():
    m = int(input('Numar de elemente = '))
    lista_locala = []
    for i in range(m):
        elem = input('Elementul' + ' ' + str(i) + ' ' + 'este:')
        lista_locala.append(elem)
    return lista_locala


# cream 3 liste citite de la tastatura
lista1 = creare_lista()
lista2 = creare_lista()
lista3 = creare_lista()
# le afisam apoi
print(lista1, lista2, lista3)


def afisare_lista(x):
    for i in x:
        print(i)


afisare_lista(lista3)"""

print('---------------------------')


def sign_up(name, email, password, is_register=False):
    if is_register:
        print('You already have an account')
    else:
        print('Please enter name, email, password...')
    print(name, email)
    print(password, is_register)


if __name__ == '__main__':  # ajuta pt a ramane printarea in consola doar pe pagina "rec_fct.py"
    sign_up('Ion', 'ion@gmail.com', '123456')
    sign_up('Maria', 'maria@gmail.com', 'ABC', is_register=True)  # putem afisa de cate ori dorim noi
    print('Hello!', end='***')
    print('Hello!')  # separatorul dintre 2 print-uri sunt stelutele, in loc sa fie pe 2 linii


# FUNCTII - sesiune 6
def cont_bancar(user, iban, pin, adresa, cont_economii, cont_credit):
    print(f'{user} ')
    print(f'{iban}')
    print(f'{pin}')
    print(f'{adresa}')
    print(f'{cont_economii}')
    print(f'{cont_credit}')
    return f'cont activ'


def log_in(user, password):
    print(f'Enter user name: {user}')
    print(f'Enter password: {password}')
    return 'Logare cu succes'


log_in_status = log_in('Dan', 1234)
print(log_in_status)
x = cont_bancar('Ion', 'RO123BTRLRON1425', 1234, 'Str. Raiului 29, Braosv', 'RO1200BTRL', 'RO130BTRL')
print(x)

