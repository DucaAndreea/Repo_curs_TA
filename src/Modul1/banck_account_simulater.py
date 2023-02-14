"""
1. Declaram expected results - user, password, sold
2. Introducem un username, manual in consola
3. Verificam corectitudinea userului
4. Introducem o parola valida
5. Verificam corectitudinea parolei
6. If all ok - 'Press enter and login'
7. Afisam mesaj string in care afisam 'expected sold'
8. Intampinam userul cu un mesaj - Cat cash doriti sa transferati?
9. Afisam in consola, daca tranzactia are loc, cat ii ramane
10. Extragem lungimea parolei
11. Lunigimea parolei <5, codul sa dea eroare - ASSERT
12. Afisam in consola usernameul, dar parola sa fie inlocuita cu * in loc de caracterele propriuzise
"""

# 1.
user = 'andreea'  # expected user
password = 'abc123'
sold= 50000

# 2.
actual_user = input('Enter username:').lower()  # action user
print(actual_user)
# 3.
assert user == actual_user

# 4.
actual_password: str = input('Enter password:').strip()
            # strip scoate spatiile din ce introducem la tastatura. ELIMINA SPATIILE
print(actual_password)

# 5.
assert password == actual_password

# 11.
len_p = len(password)
assert len_p > 5
print(f'Parola introdusa este ok!')
contains_uppercase = any(char.isupper() for char in password)
print(contains_uppercase)

# 6.
input('Press Enter and Login')

# 7.
print(f'Soldul dumneavoastra este {sold} lei.')

# 8.
cash = int(input('Ce suma doriti sa retrageti?'))
assert sold - cash >= 0
# dam update la sold
# 9.
sold = sold - cash
print(f'Tranzactia a fost efectuata cu succes. Soldul dumneavoastra este: {sold}')

# 10.
print(len(password))

# TODO checkul de parola sa il mutam la inceput
# tema: daca am introdus un spatiu, parola nu mai e corecta - sa eliminam orice spatiu, fie ca e la inceput, la sfarsit
#   sa verificam ca parola contine macar o litera mare si un caracter special
#   pct 12

a, b, c, d, e = '!', '@', '#', '%', '1'
assert a in password or b in password or c in password or d in password or e in password

