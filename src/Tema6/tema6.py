print('Clase & Obiecte')

# 1. CERC
print('----------EX1--------')
class Cerc:
    # atribute
    radius = 'raza'
    color = 'culoare'

    # constructor / obiect
    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    # metode
    def description(self):
        descriere = f'Cercul are raza {self._radius} si culoarea {self._color}'
        return descriere

    def aria(self):
        pi = 3.14
        area = pi * self._radius * self._radius
        return area

    def diametru(self):
        diam = 2 * self._radius
        return diam

    def circumferinta(self):
        p = 3.14
        d = self.diametru()
        c = p * d
        return c


cercul = Cerc(3, 'red')
print(f'Atributele:{cercul.radius} si {cercul.color}.')  # accesam atributul
print(cercul.description())  # accesam metoda
print(f'Aria cercului este {cercul.aria()}.')
print(f'Diametrul cercului este {cercul.diametru()}.')
print(f'Circumferinta cercului este {cercul.circumferinta()}.')

print('----EX2-----')


# 2. DREPTUNGHI
class Dreptunghi:

    def __init__(self, lungime, latime, culoare):
        self._lungime = lungime
        self._latime = latime
        self._culoare = culoare

    def descriere(self):
        return f'Dreptunghiul are lungimea {self._lungime}, latimea {self._latime} si culoarea {self._culoare}.'

    def arie(self):
        arie = (self._lungime) * (self._latime)
        return arie

    def perimetru(self):
        perimetru = 2 * (self._lungime + self._latime)
        return perimetru

    def alta_culoare(self, culoare_noua):
        self._culoare = culoare_noua
        print(culoare_noua)


drept = Dreptunghi(2, 3, 'Blue')
print(f'Aria dreptunghiului este {drept.arie()} si are culoarea {drept._culoare}')
print(f'Perimetrul dreptunghiului este {drept.perimetru()} si culoarea {drept._culoare}')
culoare_noua = 'White'
print(f'Dreptunghiul si-a schimbat culoarea in {culoare_noua}.')

print('-----------EX3--------')


# 3. Clasa angajat
class Angajat:
    # Atribute
    nume = ' Andreea'
    prenume = 'Duca'
    salariu = 7500

    def __init__(self, nume, prenume, salariu):
        self._nume = nume
        self._prenume = prenume
        self._salariu = salariu

    def description(self):
        return f'{self.nume}  {self.prenume} are venitul in valoare de {self.salariu} lei.'

    def nume_complet(self):
        return f'{self.nume} {self.prenume}'

    def salariu_lunar(self):
        return f'Venitul lunar este: {self.salariu} lei'

    def salariu_anual(self):
        return f'Salariual anul este {12 * (self.salariu)} lei'

    def marire_salariu(self):
        vechime = 6
        if vechime <= 3:
            print('Venitul creste cu 5%')
        elif vechime <= 6:
            print('Venitul creste cu 10%')
        else:
            print('Venitul creste cu 15%')


angajat = Angajat("Adi", "Chira", 4500)
print(angajat.description())
print(angajat.nume_complet())
print(angajat.salariu_lunar())
print(angajat.salariu_anual())
print(angajat.marire_salariu())

print('----------EX4 BONUS----------------')


# 4.
class Cont:

    def __init__(self, iBan, titular, sold):
        self._iBan = iBan
        self._titular = titular
        self._sold = sold

    # method
    def afisare_sold(self):
        afisare_sold = (f'Titularul {self.titular} are in contul {self.iBan} suma de {self.sold} lei')
        return afisare_sold

    def debitare_cont(self, suma):
        if suma < self._sold:
            self._sold -= suma
            print(f'Ati cheltuit {suma} lei. Mai aveti in cont {self._sold}')
        else:
            print('Fonduri insuficiente')

    def creditare_cont(self, suma):
        self._sold += suma
        print(f'Ati adaugat {suma} lei in cont. Aveti  {self._sold} lei.')


cont_bank = Cont('RO123BTRLRON123CRT', 'Pop Dan', 3500)
print(cont_bank.debitare_cont(8000))
print(cont_bank.creditare_cont(7500))
print('----------------------------------')

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
              [nume_nou, cantitate_noua, pret_nou, cantitate_noua * pret_nou],
              ['Ciocolata neagra', '7', '5', '35'],
              ['Ciocolata amaruie', '2', '3', 2*3]]
print(tabulate(date_tabel, headers="firstrow", tablefmt="psql", showindex="always"))
