# #Наследование
# #Полиморфизм
#
# class Airplane:
#     engine = 2
#     type_of_engine = 'turbo'
#     color = 'red'
#     fuel = 200
#     def fly(self):
#         print('FLY')
#         self.fuel = self.fuel - 5
# a320 = Airplane()
# print(a320.fuel)
# a320.fly()
# print(a320.fuel)
# class HydroAirplane(Airplane):
#     landing_type = 'water'
# h20 = HydroAirplane()
# print(h20.fuel)
# h20.fly()
# print(h20.fuel)
# print(h20.landing_type)
#

'''Задание 1
Создайте класс Human, который будет содержать
информацию о человеке.
С помощью механизма наследования, реализуйте класс
Builder (содержит информацию о строителе), класс Sailor
(содержит информацию о моряке), класс Pilot (содержит
информацию о летчике).
Каждый из классов должен содержать необходимые
для работы методы.'''


# class Human:
#     name = 'john'
#     surname = 'doe'
#     prof = 'without'
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname
#
# class Builder(Human):
#     prof = 'builder'
#     level = 'Junior'
#     def build(self):
#         print('You build something')

class Human:
    name = 'John'
    surname = 'Black'
    prof = 'without'

    def __init__(self, name, surname):
        self.name = self.name
        self.surname = self.surname


class Builder(Human):
    prof = 'builder'
    level = 'Junior'

    def build(self):
        print('This hotel was built by me')


class Sailor(Human):
    prof = 'Sailor'
    level = 'Captain'

    def sail_on_a_ship(self):
        print('I have traveled to many countries because of my work')


class Pilot(Human):
    prof = 'Pilotr'
    number_of_hours = 15000

    def fly(self):
        print('I have been flying this plain for 5 years')


class SeaBuilder(Sailor, Builder):
    pass


# jeff = Builder('Jeffry', 'Lebowski')
# jeff.build()
# print(jeff.level)
# print(jeff.prof)
# print()
# stan = Pilot('Stan', 'Miller')
# stan.fly()
# print(stan.number_of_hours)
# print(stan.prof)
# print()
# willy = Sailor('Willy', 'Wonka')
# willy.sail_on_a_ship()
# print(willy.level)
# print(willy.prof)
# print()

seal = SeaBuilder('Jack', 'Norris')
print(seal.prof)
seal.sail_on_a_ship()
seal.build()


# Полиморфизм

class Magic:
    def do_magic(self, something):
        if type(something) == type(5):
            print(something * 2)
        elif type(something) == type('5'):
            print(something + something)


m = Magic()
m.do_magic(25)
# print(type(5))
m.do_magic('12')
