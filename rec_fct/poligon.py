class Poligon:
    lungime = 0
    latime = 0

    def set_valori(self, lungime, latime):
        Poligon.lungime = lungime
        Poligon.latime = latime


#from poligon.py import *


class Dreptunghi(Poligon):
    def suprafata(self):
        return self.lungime * self.latime


#from poligon.py import*

class Triunghi(Poligon):
    def suprafata(self):
        return (self.lungime * self.latime)/2

drept = Dreptunghi()
tri = Triunghi()

drept.set_valori(30, 25)
tri.set_valori(16, 20)

print('Aria dreptunghiului este', drept.suprafata())
print(f'Aria triunghiului este {tri.suprafata()}')