# Tema Optionala

class Factura:
    seria = 'F01'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        # self._numar = numar
        self._nume_produs = nume_produs
        self._cantitate = cantitate
        self._pret_buc = pret_buc

    # metode
    def serie(self):
        print(self.seria)
        print(Factura.seria)

    def numar(self, numar):
        self._numar = numar
        return numar

    def produs(self, produs):
        self._produs = produs
        return produs

    def cantitate(self, cant):
        self._cantitate = cant
        return cant

    def pret(self, pret_buc):
        self._pret_buc = pret_buc
        return pret_buc

    def schimbare_cant(self, cantitate_noua):
        self._cantitate = cantitate_noua
        print(cantitate_noua)

    def schimbare_pret(self, pret_nou):
        self._pret_buc = pret_nou
        print(pret_nou)

    def schimbare_nume_prod(self, nume_nou):
        self._nume_produs = nume_nou


fact = Factura(1, 'Ciocolata neagra', 5, 3)
print(fact.seria)
print(fact.numar(1))
print(fact.produs('Ciocolata neagra'))
print(fact.cantitate(5))
print(fact.pret(3))

cantitate_noua = 12
print(cantitate_noua)
pret_nou = 10
print(pret_nou)
nume_nou = 'Ciocolata alba'
print(nume_nou)
import datetime
from datetime import date

from tabulate import tabulate

today = date.today()
print('Year: ', end="")
current_time = datetime.datetime.now()
print(current_time.year)
print("Month:", end="")
print(current_time.month)
print("Day:", end="")
print(current_time.day)

print(f"Factura seria {Factura.seria}.")
print(f'Data: {today}')

date_tabel = [['Produs', 'Cantitate', 'Pret_buc', 'Total'],
              [nume_nou, cantitate_noua, pret_nou, cantitate_noua * pret_nou]]
print(tabulate(date_tabel, headers="firstrow", tablefmt="psql", showindex="always"))

print("-------Ex 2 BONUS--------")


class Masina:
    marca = 'Ford'
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    color = 'Gri'
    culori_disp = {'Red', 'Negru', 'Alb', 'Galben', 'Blue'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self._model = model
        self._viteza_maxima = viteza_maxima

    # metode
    def descriere(self, marca, model, viteza_maxima, viteza_actuala, color, inmatriculata):
        descr = f'Masina {marca} este modelul {self._model}, culoare {color}, poate atinge pana la {self._viteza_maxima} km/h, iar viteza actuala este {viteza_actuala} si este {inmatriculata}'
        print(descr)
        return descr


cars = Masina
cars = Masina.descriere('Ford', 'Fiesta', 220, 0, 'Gri', False)
print(cars)
