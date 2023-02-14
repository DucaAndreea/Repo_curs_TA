# OOP - Object Oriented Programming / POO = programare orientata pe obiecte
# o CLASA este un tip nou, este definitia unui concept, ca si o reteta la paste carbonara, ADN-ul uman
# ca sa am pastele trebuie sa am un obiect
# ex. clasa Car

# un OBIECT = instanta unei clase / implementarea unui clase (ex. pastele carbonara, un om)
# facem pastele o singura date si avem 1, 3, 6, 100 portii
# ex. obiect de tip Car, pot sa am 1, 3, 6, 100 obiecte

# fields = proprietati = atribute - sunt variabilele
# ex. culoare, marca, model, consum, pret

# metode - actiuni ce pot fi facute de obiect - functii
# ex. accelereaza(), franeaza(), descideUsa(), vopsire()

class ContBancar:

    # proprietatile/atributele/fields
    def __init__(self, titularCont, iban, sold, activareCont):
        self._titularCont = titularCont
        self._iban = iban
        self._sold = sold
        self._activareCont = False

    # CONSTRUCTOR = are rolul de a impune date de start
    # ca si * din formulare, required fields
