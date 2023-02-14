# declaram o variabila in care sa stocam un float si vrem sa afisam pe ecran 2 valori cu zecimale de dupa punct

x = 50.17
# sa afisam in consola 17
print(str(x)[3:])

# sa afisam in consola 7
print(str(x)[4:])

# sa afisam in consola .17
print(str(x)[2:])

#afisam ultima cifra (7)
y = int(x * 100)
print(y)
l = y % 10
print(l)

#afisam ultimele 2 cifre (17)
n = y % 100
print(n)
