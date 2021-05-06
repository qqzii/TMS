print('\n--1--\n')

class Building:
    def __init__(self, long):
        self.long = long

    def multiply(self, mult):
        return self.long * mult

class School(Building):
    def __init__(self, childrens, long):
        self.childrens = childrens
        super().__init__(long)

    def density(self):
        return self.long / self.childrens

class Tc(Building):
    def __init__(self, profit, long2):
        self.profit = profit
        super().__init__(long2)

    def pechat(self):
        print(str(self.profit) + 'M $')


one = Building(22)
print(one.__dict__)
print(one.multiply(2))
print('-------------------')

two = School(968, 12)
print(two.__dict__)
print(two.density())
print('-------------------')

three = Tc(128, 13)
print(three.__dict__)
three.pechat()
print('-------------------')

print('\n--2--\n')

class Factorial:
    def __init__(self, a):
        self.a = a

    def __mult(self, digit, fact):
        fact *= digit
        return fact

    def calculate(self):
        count = 1
        fact_chisla = 1
        print(self.a)
        while count < self.a + 1:
            fact_chisla = self.__mult(count, fact_chisla)
            count += 1
        return fact_chisla

fact = Factorial(13)
print(fact.calculate())
# print(fact.__mult())

print('\n--3--\n')

class Bank:
    def __init__(self, name, deposit):
        self.deposit = deposit
        self.name = name

    def __add__(self, other):
        x = self.deposit + other.deposit
        return Bank('belinvest', x)

bank1 = Bank('alfa', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
bank2 = Bank('bps', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

new_bank = bank1 + bank2
print(new_bank.__dict__)
