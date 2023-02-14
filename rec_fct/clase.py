class BankAccount:

    # metoda
    def cont_bancar(self, user, iban, pin, adresa, cont_economii, cont_credit):
        print(f'{user} ')
        print(f'{iban}')
        print(f'{pin}')
        print(f'{adresa}')
        print(f'{cont_economii}')
        print(f'{cont_credit}')
        return f'cont activ'


# 'cont_bancar' este o metoda pt ca face parte dintr-o clasa, din clasa BankAccount,
# stim ca este o METODA DE INSTANTA daca primul parametru este 'SELF'.
# Ca sa apelam metoda 'cont_bancar' trebuie sa cream un OBIECT.

# obiecte
bank_account_John = BankAccount()
bank_account_Marry = BankAccount()  # instanta a clasei BankAccount
print('---------John-----')
bank_account_John.cont_bancar('John', 'RO100BTRL', 1234, 'str. Raiului 29, Brasov', 'RO123BTRL2',
                              'RO123BTRL3')  # metode
print('--------Marry-------')
bank_account_Marry.cont_bancar('Marry', 'RO101BTRL', 4758, 'str. Iadului 2, Brasov', 'RO111BTRL2',
                               'RO222BTRL3')  # metode

# Prima data OBIECTUL, apoi avem acces la orice metoda din clasa respectiva
bank_account_John.log_in('user', 'password')
