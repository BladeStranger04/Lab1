class BusPath(object):
    def __init__(self, stops, path, cost):
        self.stops = stops
        self.path = path
        self.cost = cost

    def average_distance(self):
        return str(self.path // self.stops) + ' km'

    def average_cost(self):
        return str(self.cost // self.stops) + ' Rub'


class BusPathInCity(BusPath):
    # реализация перегрузки
    def __add__(self, other):
        return other.path - self.path


class BusPathOutCity(BusPathInCity):

    def distance_from_city(self):
        return str(1000 - self.path) + ' km from city'


# example
a = BusPath(10, 150, 100)
b = BusPathInCity(5, 75, 50)
c = BusPathOutCity(2, 100, 5)

print('Пример А')
print(a.stops, a.path, a.cost)
print(a.average_distance())
print(a.average_cost())
print('_______________________')

print('Пример B')
print(b.stops, b.path, b.cost)
print(b.average_distance())
print(b.average_cost())
print(b + a)
print('_______________________')

print('Пример С')
print(c.stops, c.path, c.cost)
print(c.distance_from_city())
print('_______________________\n')


# Доп. задание
class Unit(object):
    def __init__(self, hp, dmg, armor):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor

    def attack(self, unit):
        return unit.hp - self.dmg

    def defend(self):
        self.armor += 2


class Mage(Unit):
    def __init__(self, hp, dmg, armor, mana):
        super().__init__(hp, dmg, armor)
        self.mana = mana

    def cast(self):
        self.mana -= 10


class Warrior(Unit):
    def __init__(self, hp, dmg, armor):
        super().__init__(hp, dmg, armor)
        self.armor += 3
        self.dmg += 10


unit = Unit(100, 2, 1)
war = Warrior(200, 10, 5)
mage = Mage(150, 1, 10, 100)
print('Extra\n')
print(f'Unit(Hp: {unit.hp}, Dmg: {unit.dmg}, Armor: {unit.armor})')
print(f'Hp Warrior после атаки Unit: {unit.attack(war)}')
print(f'Hp Mage после атаки Warrior: {war.attack(mage)}')
mage.cast()
print(f'Mana Mage: {mage.mana}')
war.defend()
print(f'Armor Warrior: {war.armor}')