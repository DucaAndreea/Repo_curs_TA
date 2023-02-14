data_type = "DICTIONAR"
if data_type == "lista":

    # LISTE
    print("LISTE:")
    lista1 = [1, 2, 3, 4, 5, 6]
    lista2 = ["apple", "mac", "iphone", "ipad", "apple"]
    lista3 = [1, True, 'mar', False, 5.2]

    # sliceing
    print(lista1[0], lista1[-1])  # printam primul si ultimul element din lista
    print(lista1[len(lista1) - 1])  # printam ultimul element din lista

    x = lista2.reverse()  # Reverse in place
    print(lista2)  # inversarea listei; de la coada la cap
    print(x)

    lista2.sort()
    print(lista2)

    # todo sort lista2 dupa penultimul element din string, expected result = [mac, ipad, apple, iphone]

    # lista3.sort()
    # print(lista3)

    print(lista2.count("apple"))  # arata de cate ori apare un element intr-o lista

    # todo count cate elemente sunt intr o lista mai multe decat o data, app_le (eliminam spatiile, majuscule)
    # lista.(metode de lista) to try
    # sa extragem "_" din lista mare si "ultimul 6", "2-ul din mijloc/al II-lea 2"

    x = ["a", "b", "c", "d"]
    o = x
    y = x.copy()
    u = x[:]
    y[0] = "E"

    print(x, y, u)
    print(id(x), id(y), id(u), id(o))

    lista_matrice = [lista1, lista2, lista3]
    print(lista_matrice)

    lista_mare = [lista_matrice, [0, 1, lista1, ["a", "b", "c"], [lista_matrice]], {}, True]
    print(lista_mare)
    print(lista_mare[0])
    print(lista_mare[0][0][-1])

elif data_type == "set":
    # SET
    print("SETURI:")
    my_set = {2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7}
    print(my_set)
    my_list = [1, 1, 1, 1]
    print(list(set(my_list)))
    second_set = {1, 2, 3, 5, 20, 5, 7}
    print(second_set)
    print(my_set.difference(second_set), my_set.intersection(second_set), second_set.difference_update(my_set))

elif data_type == 'tuple':
    print("TUPLURI")
    # TUPLES
    tuple = (1, 2, 5, 7)
    print(tuple[0], tuple[-1])
    # tuple[0] = 7
    print(type(tuple))
    print(type(( )))

elif data_type == "DICTIONAR":
    print("DICTIONAR:")
    dictionar = {
        "user1": "admin",
        "user2": "Petre",
        "user3": {
            "name": "John",
            "email": "john@john.com",
            "isActive": True
        }
    }
    print(dictionar["user2"], dictionar["user3"]["email"])

    # TODO desplay John and his email only his isActive is True
    # creati un dictionar mai complex cu date primite ptr keym ptr valori lista de actionare cu tuple, set

myDict = {
    'animal': 'pisica',
    123: 'thisisanumber',
    True: [
        {
            'user': 'rares',
            'parola': 'andrei',
        },
        {
            'user': 'ion',
            'parola': 'marcel',
        }
    ],
    52.2: 'latitudinea Romaniei'
}
my_dict2 = dict(animal='pisica', numbers='thisisanumber',
                myboolean=[dict(user='rares', parola='andrei'), dict(user='ion', prola='marcel')],
                parola={
                    1: 1,
                    True: 'yes'
                }
                )

print(myDict)
print(myDict[True][1]['parola'])  # am printat parola 'marcel' din dict

myDict["email"] = "gmail@gmail.com"  # adaugare elem nou in Dictionary
myDict["email"] = "yahoo@yahoo.com"  # am inlocuit gmail@... cu yahoo@...
print(myDict)

del myDict['email']  # am sters cheia 'email'
print(myDict)
