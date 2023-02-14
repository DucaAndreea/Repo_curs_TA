# exersare:
class Dog:
    # Class attribute
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name  # creeaza un atribut numit 'name' si ii atribuie valoarea name parametrului
        self.age = age  # creeaza un atribut 'age' si ii atribuie valoarea age parametrului

    # Instance method
    def description(self):
        return f'{self.name} is {self.age} years old'

    # Another instance method
    def speak(self):
        sound = 'Woof Woof!'
        return f'{self.name} says {sound}'


maya = Dog("Maya", 9)
puffy = Dog("Puffy", 4)

print(maya.name)  # Maya
print(puffy.name)  # Puffy
print(maya.age)  # 9
print(puffy.age)  # 4
print(maya.species)  # Canis familiaris
print(puffy.species)  # - || -

maya.age = 12  # atributul 'age' l-am modificat in obiectul '12'
print(maya.age)

puffy.species = 'Felis silvestris'  # atributul 'species' l-am modificat in obiectul 'Felis silvestris'
print(puffy.species)

print(maya.description())  # Maya is 12 years old
print(maya.speak())  # Maya says Woof Woof!
