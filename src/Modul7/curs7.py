'''OOP:
-incapsulare
-mostenire
-abstractizare
-polimorfism
'''
from abc import ABC

'''
Exceptii:
-cand codul nu poate executa instruct
-codul arunca o exceptie
-progr se pot astepta la ea, pot sa o 'prinda' si sa o 'trateze'
-putem anticipa errori si evitam sa 'crape' aplicatia
-se foloseste sintaxa try/except
-uneori dorim sa 'ridicam' o exceptie intentionat
'''

try:  # in try punem codul 'periculos'
    lista = [1, 2, 3]
    lista[6]
except IndexError as e:  # tratam IndexError exception
    print(e)
'''
1.MOSTENIRE / Inheritance
= O CLASA PARINTE poate fi mostenita de oricate clase copil
-aceste clase copil vor avea accea la toate atributele si metodele clasei parinte
'''


class Chef:  # clasa parinte
    def make_salad(self):
        print('salad')

    def make_fries(self):
        print('fries')


# clasa copil care mosteneste clasa Chef (se trece intre () numele clasei parinte)
class JapaneseChef(Chef):
    def make_sushi(self):
        print('sushi')


class ItalianChef(JapaneseChef):  # copilul JaponezuluiChef, poate accesa si sushi si salad si fries
    def make_pizza(self):
        print('pizza')


'''POLIMORFISM / Polymorphism
- cand exista 2 functii cu acelasi nume dar au un comportament diferit
'''


# Polymorphism with class methods
class Romania():
    def language(self):
        print('Romanian')


class USA():
    def language(self):
        print('English')


obj_ro = Romania()
obj_usa = USA()

for country in (obj_ro, obj_usa):
    country.language()


# Polymorphic function
def add(x, y, z=0):
    return x + y + z


print(add(2, 3))
print(add(2, 3, 4))

# ex de built in poly function
print(len("abc"))

'''ABSTRACTIZARE / Abstraction
=o clasa abstr contine metode FARA CORP, dar si metode cu LOGICA DEFINITA
- o interfata contine doar metode abstracte
- aceste clase vor fi mostenite de clasele copil care vor trebui sa scrie logica metodelor
-"Dog() class implements the Animal() Interface"
- clasa parinte e ca o reteta ce trebuie implementata exact asa de catre toti mostenitorii
'''


class Animal(ABC):  # daca e abstract punem (ABC)

    @abstractmethod  # metode abstracte definite
    def sound(self):
        raise NotImplementedError

    @abstractmethod  # = decorator
    def sleep(self):
        raise NotImplementedError


class Dog(Animal):
    def sound(self):
        print('Ham! Ham!')

    def sleep(self):
        print('Zzzz!')

'''INCAPSULARE / Encapsulation
- in general, ca sa nu aglomeram optiunile utilizatorului, atributele se ascund
-in loc sa vada toate fields si methods va vedea doar metodele
-pastram codul clean
- metodele care nu se doresc a fi expuse pot fi ascunse
-se folosesc sintaxa_fieldName sau _methodName
'''

class Car:
    __color = 'gray' # __ face sa fie ascuns 'color'

    def get_color(self): # folosim getter sa afisam culoarea
        return self.__color

    def set_color(self, culoarea_dorita): # folosim setter ca sa setam o alta culoare
        self.__color = culoarea_dorita

    def __hidden(self):
        pass


#TODO: creaza un pachet numit "car" si fiecare clasa sa fie mutata intr-un fisier nou (clasa - model)
#TODO: crearea unui miniproiect pe princip OOP care sa simuleze teste