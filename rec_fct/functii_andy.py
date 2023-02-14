'''
a compila = a traduce codul din sintaxa unui limbaj de programare in machine language
Python - loosly typed ; nume = 'Andreea'
Java - strongly typed -> specificam tipul de date; string nume = 'Andreea'

variabile = valori tinute in zona de memorie
variabilele sunt de diferite tipuri de date:
    char (un sg caracter),
    string - un sid de caractere delimitate de '' sau ""
    int - nr intregi
    float - nr zecimal 3,33
    double - ne zecimal cu mai multe nr 3,33333
    byte - nr mai mic, merge pana la 100 si ceva, de ex varsta unui om

Operatori
= op de atribuire x = 3
logici, aritmetici si de comparare

Structuri de date
array - dimensiune fixa, index incepe de la 0, len()
liste - dimensiune dinamica, index incepe de la 0, len()
map, dict -0 structura cheie: valoare; cnp: nume, elev: nota

Flow control
if else, switch

Loop
while - repeta un bloc de cod atat timp cat conditia e True
for - se foloseste cand stim cate repetari sa facem, 101 dalmatieni
    parcurgere array cu ajutorul lui i (indexul)
for each - pt fiecare masina din masini

'''

# o Functie este o logica delimitata care poate fi refolosita
# (de unde pana unde? trebuie in interior sa aiba o logica, scopul este ca poate fi refolosita)


# o functie simpla care ne printeaza ceva pe ecran si nu returneaza nimic
# nu ne da nici un raspuns (nu are return)
# nu are parametri

# NU PUTEM FOLOSII SPATII IN NUME (camel case sau snake case)
# nu putem defini o f in alta f (nu pot instala firefox in chrome)


# CTRL + Click pe functie => ne duce la corpul ei

# o functie care saluta clientul in f de numele lui, sunt necesari parametrii

def printGretting():
    print('Buna ziua! Bine ati venit')

def printGrettingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')

def mediaNr(a, b, c):
    return (a + b + c)/3

def piValue():
    return 3.14
    print('abc')

# exercitiu:  daca nr e pozitiv returnati True, altfel fals

def nrPozitiv(numar):
    if numar >= 0:
        return 'Numarul este pozitiv'
    else:
        return 'Numarul NU este pozitiv'

# daca persoana e majora

def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False


# zona de apelare:
printGretting()
printGretting()
printGrettingByName('D', 'Andreea')
printGrettingByName('D', 'Mihai')
print(mediaNr(3,3,4))
print(piValue())
print(verificareMajor(-2))
print(nrPozitiv(-3))

age = int(input('introduceti varsta dvs:'))
if verificareMajor(age):
    print('Cont creat. Bine ai venit in aplicatie!')
else:
    print('Nu ai 18 ani!')

# oop - variabile (atribute, proprietati sau fields) si functii (metode)