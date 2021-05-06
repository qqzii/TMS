class Wood:
    def __init__(self, years, height):
        self.years = years
        self.height = height

    def plus_size(self, how_plus):
        self.height += how_plus

dub = Wood(140, 18)

print('Дерево')
print(dub.__dict__)

dub.plus_size(22)
print(dub.__dict__)

class Man:
    def __init__(self, mass, height, race, eaten_candy):
        self.mass = mass
        self.height = height
        self.race = race
        self.eaten_candy = eaten_candy

    def eat(self, sweet):
        self.eaten_candy.append(sweet)

me = Man(64, 173, 'europioid', ['rak', 'bjilki', 'bird milk'])

print('Человек')
print(me.__dict__)

me.eat('woo')
print(me.__dict__)

class Book:
    def __init__(self, pages, name, cover):
        self.pages = pages
        self.name = name
        self.cover = cover

    def riding(self, index_page):
        print(self.pages[index_page])

first = Book(['Колобок', 'повесился'], 'Kolobock', 'paper')
second = Book(['Арагорн - король Гондора', 'Гимли - гордый гном', 'Леголас - принц лихолесья', 'Фродо - тихий хоббит из Шира',], 'Silmarillion', 'cardboard')

print('Книга')
first.riding(0)
first.riding(1)
second.riding(3)

class Convert:
    def __init__(self, convert, text, sender):
        self.convert = convert
        self.text = text
        self.sender = sender
    def signa(self, app_sign):
        print(self.text + '\nС уважением, ' + app_sign)
one = Convert('paper', 'Привет, у меня все хорошо\nДоехал до Таллина отлично, без долгих остановок', 'mom')

print('Конверт\n')
one.signa('Артем')

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def plus_day(self, plus):
        error = False
        if self.month > 12 or self.month <= 0:
            error = True
        if self.day <= 0:
            error = True
        if self.month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
            if self.day > 31:
                error = True
        else:
            if self.month != 2:
                if self.day > 30:
                    error = True
            else:
                if self.year % 4 == 0:
                    if self.day > 29:
                        error = True
                else:
                    if self.day > 28:
                        error = True
        if error == True:
            print('Введена некорректная дата...')
        else:
            self.day += plus
            while self.day > 31:
                if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
                    if self.day > 31:
                        self.month += 1
                        self.day -= 31
                else:
                    if self.month != 2:
                        if self.day > 30:
                            self.month += 1
                            self.day -= 30
                    else:
                        if self.year % 4 == 0:
                            if self.day > 29:
                                self.month += 1
                                self.day -= 29
                        else:
                            if self.day > 28:
                                self.month += 1
                                self.day -= 28
            while self.month > 12:
                self.year += 1
                self.month -= 12
        print('Новая дата')
        print(nowaday.__dict__)

nowaday = Date(1, 4, 2001)

print('\nДата')
print(nowaday.__dict__)

nowaday.plus_day(216)
