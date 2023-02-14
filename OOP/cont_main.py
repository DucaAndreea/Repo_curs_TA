from OOP.cont_bancar import ContBancar

cont1 = ContBancar('Andreea Duca', 'RO001')
cont2 = ContBancar('Mihai Duca', 'RO002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)


cont1.alimentareCont(3500)
cont2.alimentareCont(9500)

cont1.interogareSold()
cont2.interogareSold()

cont1.plataCard(7800)
cont2.plataCard(3500)

# tema: clasa Angajat
# nume, prenume, salariu, vechime
# constructor: nume, prenume, salariu, functie, vechime
# metode: descriere (cutarica are sal vechime....), marire salariu in f de vechime