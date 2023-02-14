# Tema 1
# 1. O variabila este ca si o cutiuta in care se acumuleaza date.

# 2.
grupa = "Buburuzelor"  # string
print(grupa)

nr_gr = 25  # int
print(nr_gr)

media_varstei = 2.6  # float
print(media_varstei)

prezenta = True  # bool
print(prezenta)

# 3.
print(type(grupa))  # <class 'str'>
print(type(nr_gr))  # <class 'int'>
print(type(media_varstei))  # <class 'float'>
print(type(prezenta))  # <class 'bool'>

# 4.
print(round(media_varstei))
print(type(media_varstei))

media_varstei = round(2.6)
print(type(media_varstei))  # <<class 'int'>

# 5.
print(f'Grupa {grupa} este grupa mare')  # Grupa Buburuzelor este grupa mare
print(f'Grupa {grupa} este formata din {nr_gr} de copilasi')  # Grupa Buburuzelor este formata din 25 de copilasi
print(f'Media de varsta a grupei este {media_varstei}')  # Media de varsta a grupei este 3
print(f'Prezenta s-a facut de dimineata. {prezenta}')  # Prezenta s-a facut de dimineata. True

# 6.
numele = input('introdu numele:')  # Duca
prenumele = input('introdu prenumele:')  # Andreea
print('Numele complet are ', len(numele) + len(prenumele), 'caractere')  # Numele complet are  11 caractere

# 7.
x = int(input('Introdu lungimea dreptunghiului'))  # 5
y = int(input('Introdu latimea dreptunghiului'))  # 4
print('Aria dreptunghiului este', x * y)  # Aria dreptunghiului este 20

# 8.
str = ('Coral is either the stupidest animal or the smartest rock')
print(str)
# 9.
print(str.count('the'))  # =>3

# 10.
assert str != int
