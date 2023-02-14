def cont_bancar(user, iban, pin, adresa, cont_economii, cont_credit):
    print(f'{user}')
    print(f'{iban}')
    print(f'{pin}')
    print(f'{adresa}')
    print(f'{cont_economii}')
    print(f'{cont_credit}')
    return "cont activ"


def log_in(user, password):
    print(f'Please enter your user name: {user}')
    print(f'Please enter your password: {password}')
    return "Succesful log in"


def generate_report(report):
    print(f'<h1>{report}</h1>')


log_in_status = log_in('Petre', 1234)
print(log_in_status)
generate_report(log_in_status)
x = cont_bancar('Popescu', 'RO100BTRL', 7777, 'Str. Raiului nr. 12 Bucuresti', 'RO1200BTRL', 'RO130000BTRL')
print(x)
