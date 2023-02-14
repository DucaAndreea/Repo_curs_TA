# Tema 4 - loop
# 1.
from typing import List

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat',
          'Trabant', 'Opel']
for masina in masini:
    print(f'Masina mea preferata este {masina}')

for i in masini:
    print(i)
else:
    print('am terminat')

while masina in masini:
    print(f'Masina preferata este {masina}')
    masina += 'Audi'
else:
    print('am terminat')

#2
for masina in range(2, len(masini)):
    masina -= 1
    print(masini[masina].upper())
else:
    print(masina)

#3
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat',
          'Trabant', 'Opel']

for masina in masini:
    if masina == 'Mercedes':
        print('am gasit masina dorita de dvs')
        break
    else:
        print('nu am gasit masina dorita, mai cautam')

# 4
for masina in masini:
    if masina == 'Trabant':
        continue
    elif masina == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

# 5
#print(masini)
masini_vechi = []
for masina in masini:
    if 'Lastun' in masini:
        masini.remove('Lastun')
        masini_vechi.append('Lastun')
        #print(masini_vechi)
        #print(masini)
    elif 'Trabant' in masini:
        masini.remove('Trabant')
        masini_vechi.append('Trabant')
        masini.append('Tesla')
        #print(masini_vechi)
        #print(masini)
print(f'Modelele noi de masini sunt: {masini}')
print(f'Modelele vechi sunt: {masini_vechi}')

# 6.
pret_masini = {
    'Dacia': 68000,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget = 15000
for k, v in pret_masini.items():
    if v <= buget:
        print('Pentru bugetul alocat aveti posibilitatea', k, 'in valoare de', v, 'euro')
    else:
        print('Pentru un buget de sub 15000 euro puteți alege mașina Lastun')

# 7
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(numere.count(3)) # 3 apare de 4 ori
for i in numere:
    numar = i+1
    print(i)
# 8
lista1 = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for ele in range(0, len(lista1)):suma = suma + lista1[ele]
print('Suma este', suma) # 30
#9
#10
