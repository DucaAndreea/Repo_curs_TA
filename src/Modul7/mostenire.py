from abc import ABC, abstractmethod


class CarModel(ABC):
    @abstractmethod
    def volan(self):
        raise NotImplemented

    @abstractmethod
    def roti(self):
        raise NotImplemented

    @abstractmethod
    def scaune(self):
        raise NotImplemented

    def sistem_audio(self):
        print('Avem sistem audio')

class OldCar(CarModel): # clasa parinte

    def __pilot_automat(self): #metoda privata pt ca am pus __ inainte de pilot_automat
        print('Bunicu e pilotul automat')

    def _valoare_sentimentala(self):   # metoda protected
        self.__pilot_automat()
        print('Masina de colectie')


# met privata are acces orice alta metoda din clasa, met protected ai acces si din clasa care mostensete clasa resp - CRED
    def scaune(self):  # metode publice
        print('4 locuri')

    def volan(self):   # metode publice
        print('Masina are volan pe staga')

    def motor(self):    # metode publice
        print('Masina are motor disel')

    def roti(self):   # metode publice
        print('Masina are roti de lemn')


class NewCar(OldCar):
    def roti(self):
        print('Are roti de sticla')

    def oglinzi(self):
        print('Masina are 5 oglinzi')

    def areABS(self):
        print('Are ABS')

    def airbag(self):
        print('Are 5 airbag-uri')

    def extra_optiuni(self):
        self._valoare_sentimentala()


class BritishCar(NewCar):
    def volan(self):
        print('Volan pe dreapta')

    def gps(self):
        print('Are GPS')

class AlienCar(CarModel):

    def roti(self):
        print('Are si roata de rezerva')

    def scaune(self):
        print('Are 5 scaune')

    def volan(self):
        print('Volan cu comenzi')


# obiecte:
dacia = OldCar()
renault = NewCar()  # am accest si la fct din OldCar (volan, motor, roti)
british_renault = BritishCar()
aliencar = AlienCar()

print('Dacia:')
dacia.scaune()
dacia.roti()
dacia.motor()
dacia.volan()
print('Renault:')
renault.roti()
renault.motor()
renault.volan()
renault.oglinzi()
renault.areABS()
renault.airbag()
print('British car:')
british_renault.gps()
british_renault.volan()
renault.volan()
renault._valoare_sentimentala()
print('Alien car:')
aliencar.volan()
aliencar.scaune()
aliencar.roti()
