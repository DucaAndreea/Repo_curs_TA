class ContBancar:
    # constructor, atribute definite prin constructor
    def __init__(self, titularCont, iban):
        # atribute, fields
        self.titularCont = titularCont
        self.iban = iban
        self.sold= 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0

    #metode
    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'Iban: {self.iban}')
        print(f'Sold:{self.sold}')
        print(f'Status cont{self.activ}')
        print(f'Nr de incercari {self.incercari_activare}')
        print('--------------------------')

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('Card activat cu succes!')
            self.activ = False
        else:
            print('PIN incorect')
            self.incercari_activare = self.incercari_activare + 1
           #self.incercari_activare+=1

    def alimentareCont(self, suma):
        self.sold += suma
        print(f'Ati alimentat {suma} lei. Aveti in cont {self.sold}')

    def plataCard(self, suma):
        # variabile scope
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'ati cheltuit {suma}.Mai aveti {self.sold}')

        else:
            print('Fonduri insuficiente!')


    def salut(self):
        print(f'Buna {self.titularCont}')