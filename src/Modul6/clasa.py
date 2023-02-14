class BankAccount:
    bank_name = 'Banca Transilvania'

    def __init__(self, user, pwd):
        self._user = user  # '_user' nu-i acelasi lucru cu 'user'
        self._pwd = pwd

    def cont_bancar(self, iban, adresa, cont_economii, cont_credit):
        print(
            f'Hi {self._user}!, Ibanul dv: {iban}, cu codul PIN: {self._pwd}, Adresa dv: {adresa}, {cont_economii}, {cont_credit}')

        return "cont activ"

    def log_in(self):
        print(self.bank_name)
        print(BankAccount.bank_name)
        return f'{self._user} log in with {self._pwd}'

    def interogare_sold(self, sold):
        status_log_in = self.log_in()
        if status_log_in == 'Andreea log_in with 0000':
            print(f'Soldul {self._user} este {sold}')
        else:
            print('User inexistent')

    @staticmethod
    def curs_valutar(moneda):
        if moneda == 'EURO':
            print('4.94')
        elif moneda == 'USD':
            print('4.5')
        else:
            print('Curs inexistent pt moneda asta')


bank_account_John = BankAccount('John', '123')  # obiect1
bank_account_Marry = BankAccount('Marry', '456')  # obiect2
bank_account_John.cont_bancar('RO100BTRL', 'Str. Raiului nr. 12 Bucuresti', 'RO1200BTRL',
                              'RO130000BTRL')  # metode
bank_account_Marry.cont_bancar('RO100BTRL', 'Str. Iadului nr. 12 Bucuresti', 'RO1200BTRL',
                               'RO130000BTRL')

log_in_status = bank_account_John.log_in()
print(log_in_status)
bank_account_John.interogare_sold('20.000 RON')


bank_account_John.curs_valutar('EURO')