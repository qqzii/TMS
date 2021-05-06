class Man:
    def __init__(self, mass, height, race):
        self.mass = mass
        self.height = height
        self.race = race

me = Man(64, 173, 'europioid')
mom = Man(52, 158, 'europioid')

print('Человек')
print(me.__dict__)
print(mom.__dict__)

class Wood:
    def __init__(self, years, height):
        self.years = years
        self.height = height

bereza = Wood(12, 24.2)
dub = Wood(140, 18.0)

print('Дерево')
print(bereza.__dict__)
print(dub.__dict__)

class House:
    def __init__(self, cost, meters, tenants):
        self.cost = cost
        self.meters = meters
        self.tenants = tenants

dacha = House(20000, 25.2, 1)
kvartira = House(120000, 82.3, 3)

print('Дом')
print(dacha.__dict__)
print(kvartira.__dict__)

class Book:
    def __init__(self, pages, name, cover):
        self.pages = pages
        self.name = name
        self.cover = cover

first = Book(12, 'Kolobock', 'paper')
second = Book(4513, 'Silmarillion', 'cardboard')

print('Книга')
print(first.__dict__)
print(second.__dict__)

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

birthday = Date(1, 11, 2000)
nowaday = Date(23, 4, 2020)

print('Дата')
print(birthday.__dict__)
print(nowaday.__dict__)

class Convert:
    def __init__(self, convert, content, sender):
        self.convert = convert
        self.content = content
        self.sender = sender

one = Convert('paper', 'toy', 'mom')
two = Convert('paper', 'check', 'dad')

print('Конверт')
print(one.__dict__)
print(two.__dict__)
