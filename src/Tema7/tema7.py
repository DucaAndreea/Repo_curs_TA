# Tema 7
from abc import ABC
# Abstraction
class FormaGeometrica(ABC):
    pi = 3.14
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi')

# Inheritance (mostenire)
class Patrat(FormaGeometrica):

    def __init__(self, latura): # constructor latura
        self.__latura = latura

    @property
    def latura(self, value):
        self.__latura = value

    @latura.setter
    def latura(self, value):
        self.__latura = value

    @latura.deleter
    def latura(self):
        del self.__latura

    def aria(self):
        return self.__latura ** 2

    def descrie(self):
        print("Eu am colturi")

# Encapsulation
# class Patrat:
#     __color = 'Rosu'
#
#     def get_color(self):
#         return self.__color
#
#     def set_color(self, culoarea_noua):
#         self.__color = culoarea_noua

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, value):
        self.__raza = value

    @raza.deleter
    def raza(self):
        del self.__raza

    def aria(self):
        return self.pi * self.raza ** 2

    def descrie(self):
        print("Eu nu am colturi")

# Polymorphism
class Sfera():

    def new_form(self):
        print('Eu sunt o sfera')

class Cilindru():

    def new_form(self):
        print('Eu sunt un cilindru')

new_form = Sfera()
new_form = Cilindru()

p = Patrat(3)
print(p.aria())
p.descrie()

c = Cerc(2.5)
print(c.aria())
c.descrie()

s = Sfera()
print(s.new_form())

