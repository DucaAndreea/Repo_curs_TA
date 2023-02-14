my_list = ['unu', 2, 3, 4, True, dict(name='John'), set(), 100, {'key1': 1, 'key2': 2, 'key3': 3}]
# for i in lista:
#     if isinstance(i, str):
#         print(i)
#     if isinstance(i, int):
#         print(i)
#     elif isinstance(i, dict):
#         print(i["name"])
#     else:
#         print('print other')

# for i, v in enumerate(my_list):
#     print(i, v) # pe o coloana este indexul, pe alta coloana sunt elementele
#     print(my_list[i])

# for i in range(len(my_list)):
#     if isinstance(my_list[i], dict):
#         print(my_list[i])

for i in range(len(my_list)):
    if isinstance(my_list[i], dict):
        for k, v in my_list[i].items():
            if k == "key3" and v == 3:
                print(k, v)
for i in range(100, 0, -2):
    print(i)
# TODO: declaram o lista ce contine doar nr, vrem sa facem suma numerelor din lista prin
#  4 metode (for, for dupa index, count)
# sa gasim dublicatele dintr-o lista [ion, petre, ion etc] --> sa afiseze doar un ion

tema_lista = ['ion', 'ion', 'mihai', 'radu', 'mihai', 'mihai']
# o lista cu diverse nr, sa obtinem cel mai mare nr par
print(tema_lista.count('ion')) # apare de 2 ori
print(tema_lista.count('mihai')) # 3 ori
