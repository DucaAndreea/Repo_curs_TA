def sign_up(name, email, password, is_register=False, *home_details, **work_details):
    print(work_details['Street'])
    print(work_details['House_nr'])
    print(work_details['City'])
    if is_register:
        print('You already have an acount')
    else:
        print('Please enter name, email, password...')
        for h in home_details:
            print(h)
    print(name, email)
    print(password, is_register)


def get_user(*address):
    # print(address[0])
    for a in address:
        print(a)


def get_max_score(students):
    max_g = 0
    students = [{'name': 'Ion', 'grade': 5}, {'name': 'Maria', 'grade': 7}]
    for s in students:
        for n, g in s.items():
            if n == 'grade':
                print(n, g)
                if g > max_g:
                    max_g = g
    return max_g


print(get_max_score(''))

if __name__ == '__main__':  # apare in consola doar cand sunt in functii.py, nu si cand rulez rec_fct2.py
    sign_up('Ion', 'ion@gmail.com', 'abcd', is_register=True, Street='Rue de Paris', House_nr=20, City='Paris')
    sign_up('Maria', 'maria@gmail.com', '1425', False, 'Calea Dorobantilor', 70, 'copsa mica', Street='teleorman',
            House_nr=45, City='Cj')
    get_user('Calea Constantei', 'str Timisului', 'str XYZ')

    # print('Hello', end='***')
    # print()
    # print('Hello!', 'world', 'Hello Wold John', sep='@')
    # print('Hello', 'world', 'Hello World John')

# TODO: printam studentul cu max grade, schimbam lista de dict sa fie transmisa ca argument
