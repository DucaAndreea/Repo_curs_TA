try:
    my_list = [1, 2, 3]
    print(my_list[3])
except IndexError as e:
    print(e) # => list index out of range
finally:
    print('Orice ar fi se printeaza')

try:
    print(x)
except NameError:
    print('X is not defind.')
finally:
    print('Create the X')
