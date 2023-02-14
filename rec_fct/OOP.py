# OOP = Object Oriented Programming = programare orientata spre obiect

'''CLASA:
O CLASA este o reteta (blueprint) pt crearea obiectelor
- contine elemente DESCRIPTIVE: atribute/fields (practic niste variabile)
- contine actiuni posibile: metode (practic niste functii)
- SELF - este instanta clasei, AJUTA functia sa aiba acces la atributele clasei

Deci o clasa este doar un concept, cum ar fi o reteta de paste carbonara, Faptul ca exista reteta
NU inseamna ca exista si pastele, dar aceeasi reteta o putem folosi sa facem 1, 2, 3, 100 portii carbonara.

Atributele clasei sunt definite direct sub prima linie a numelui clasei și sunt
indentate cu patru spații. Trebuie să li se atribuie întotdeauna o valoare inițială.
Când este creată o instanță a clasei, atributele clasei sunt
create automat și atribuite valorilor lor inițiale.

Utilizați atributele de clasă pentru a defini proprietăți care ar trebui să aibă aceeași valoare
pentru fiecare instanță de clasă.
Utilizați atribute de instanță pentru proprietăți care variază de la o instanță la alta.
'''


class Car:
    # fields (atribute)
    make = 'Dacia'
    model = None
    year = 2022
    color = None

    # metode
    def accelerate(self):
        print('Vruum! Vruum!')

    def stop(self):
        print('STOP!')

    # constructor / obiect
    def __init__(self, model, color):
        self.model = model
        self.color = color


''' OBIECT:
OBIECT = INSTANTA A CLASEI
toate obiectele de tip Car vor avea: - acelasi comportament
                                    - aceleasi atribute (pot suferi modificari dupa initializarea obiectului)
                                    - aceleasi metode
             ex: o masina se poate vopsi intr-o culoare noua
-putem crea oricate obiecte de tip Car dorim
-acesta este si avantajul OOP: write once, use n times
'''
# car1 = Car()  # initializam obiecte de tip Car
# car2 = Car()  # car2 este instanta a clasei Car

car1 = Car('Duster', 'white')
car2 = Car('Logan', 'blue')

print(car1.make)  # dupa . avem acces la fields/atribute
print(car2.make)
car1.model = 'Duster'  # putem SUPRASCRIE valori
car2.model = 'Logan'
car1.accelerate()  # dupa . avem acces la methods
car2.accelerate()
car1.stop()
car2.stop()
print(car1.model)

'''CONSTRUCTOR
CONSTRUCTOR se asigura ca la crearea obiectelor setam niste date fara de care obiectul nu are sens sa existe.
- practic atribuie valori atributelor

- daca ne gandim la un formular, ar fi acele field-uri cu * care sunt obligatorii

- daca prin constructor suntem obligati sa dam model si color, nu am putea sa instantiem obiecte de tip Car fara sa 
dam aceste valori obligatorii
'''

car1 = Car('Duster', 'white')
car2 = Car('Logan', 'blue')
print(car1.make)  # Dacia
print(car1.model)  # Duster
print(car1.color)  # white

# CUM IMPORTAM CLASE DIN ALTE FISIERE?
# from folder1.car import Car

'''
Producător: X
Model: XYZ
Înălțime: 1.2m
Lățime: 0.5m
Adâncime: 0.4m
Capacitate de spălare: 8kg
Număr de programe: – 15
Buton de: Pornire/Oprire/Pauză

Bineînțeles că fiecare produs are mult mai multe caracteristici ori funcții diferite sau nu, 
însă orice mașină de spălat le deține și pe acestea.
Deci, putem defini o clasă de obiecte numită mașină_de_spălat.
Am căutat pe Internet... Bosch WAN28108GB, Indesit IWC8125, Beko WTG841 
sunt mașini de spălat rufe cu anumite caracteristici. 
Toate însă fac parte din aceeași clasă numită de noi ca exemplu - mașină_de_spălat.

Prin încapsulare înțelegem mecanismul prin care DATELE/ATRIBUTE (VARIABILELE/FIELDS)
și FUNCTIILE (numite în acest caz și METODE) sunt plasate împreună, într-o
unică structură, numită CLASA.


Atunci când un constructor creează o nouă mașină de spălat, este realizat
un nou obiect al clasei mașină_de_spălat, care este o instanțiere a
acesteia. Clasa este doar o structură abstractă.

ACCESUL LA METODELE unei clase se realizează utilizând operatorul punct ".":

    obiect.metoda(argumente)
    
O metodă a clasei respective poate sau nu să întoarcă un rezultat. Mai sus
ne specifică o valoare de adevăr, însă altele pot avea rolul doar de a
prelucra informația. De asemenea, argumentele pot lipsi, depinde doar de
definiția metodei.

Atenție. Metoda is_integer() aparține clasei float. Dacă încercați să o
apelați pentru un obiect de tip int, veți obține eroare.

REȚINEȚI!
Un obiect este instanțierea unei clase efectuată de un constructor.
Clasa are încapsulate date și metode proprii care sunt structurate abstract.

'''


# Clase
class Dog:
    pass  # keyword; folosit ca substituent indicand unde va ajunge codul in cele din urma

    # Class attribute
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name  # creeaza un atribut numit 'name' si ii atribuie valoarea name parametrului
        self.age = age  # creeaza un atribut 'age' si ii atribuie valoarea age parametrului

 # Instance method
    def description(self):
        return f'{self.name} is {self.age} years old'

    # Another instance method
    def speak(self):
        sound = 'Woof Woof!'
        return f'{self.name} says {sound}'
'''
Atributele create în .__init__()sunt numite atribute de instanță . 
Valoarea unui atribut de instanță este specifică unei anumite instanțe a clasei. 
Toate Dog obiectele au un nume și o vârstă, dar 
valorile pentru atribute name și age vor varia în funcție de Dog instanță.

Pe de altă parte, atributele de clasă sunt atribute care au aceeași valoare pentru
toate instanțele de clasă. 
Puteți defini un atribut de  clasă atribuind o valoare unui nume de variabilă în afara .__init__().

Atributele clasei sunt definite direct sub prima linie a numelui clasei și sunt 
indentate cu patru spații. 
Trebuie să li se atribuie întotdeauna o valoare inițială. 
Când este creată o instanță a clasei, atributele clasei sunt 
create automat și atribuite valorilor lor inițiale.
'''

maya = Dog("Maya", 9)
puffy = Dog("Puffy", 4)

print(maya.name) # Maya
print(puffy.name) # Puffy
print(maya.age) # 9
print(puffy.age) # 4
print(maya.species) # Canis familiaris
print(puffy.species) # - || -

maya.age = 12 # atributul 'age' l-am modificat in obiectul '12'
print(maya.age)

puffy.species = 'Felis silvestris' # atributul 'species' l-am modificat in obiectul 'Felis silvestris'
print(puffy.species)

print(maya.description()) # Maya is 12 years old
print(maya.speak()) # Maya says Woof Woof!


''' Metode de instanta / Instance method
Metodele de instanță sunt funcții care sunt definite în interiorul 
unei clase și pot fi apelate doar dintr-o instanță a acelei clase. 
La fel ca .__init__(), primul parametru al unei metode de instanță 
este întotdeauna self.
'''
