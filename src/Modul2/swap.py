x = 9
y = 7

a = x
x = y
y = a
print(x, y)

x, y = y, x
print( x, y)

x = x + y
y = x - y
x = x - y
print(x, y)

# TODO cum am putea face cu inmultire si impartire?