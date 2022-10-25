import random

# consts
value_of_items = {'в': (3, 25), 'п': (2, 15), "б": (2, 15), "а": (2, 20), "и": (1, 5),
                  "н": (1, 15), "т": (3, 20), "о": (1, 25), "ф": (1, 15), "д": (1, 10), "к": (2, 20), "р": (2, 20)}

items = list(value_of_items.keys()) # список предметов


backpack = {'и'} # так как том болеет астмой обязательно должен быть ингалятор, берём его первым
space_of_backpack = 1 # смотрим место в рюкзаке
all_variants = [] # +- все варианты
correct_varriants = [] # подошедшие варианты
last = '' # последний добавленный предмет

# просто перебираем рандомно варианты
for i in range(10000):
    if space_of_backpack > 9:
        backpack.remove(last)
        space_of_backpack -= value_of_items.get(last)[0]
        if space_of_backpack == 9:
            if backpack not in all_variants:
                points = 15
                for it in value_of_items:
                    if it not in backpack:
                        points -= value_of_items.get(it)[1]
                    else:
                        points += value_of_items.get(it)[1]
                if points > 0:
                    correct_varriants.append(backpack)
        space_of_backpack = 1
        backpack = {'и'}
    item = random.choice(items)
    if item not in backpack:
        space_of_item = value_of_items.get(item)[0]
        last = item
        backpack.add(item)
        space_of_backpack += space_of_item
print(len(correct_varriants))
# выдаём любой подходящий вариант
any_backpack = random.choice(correct_varriants)
points = 15
bp = []
for it in value_of_items:
    if it not in any_backpack:
        points -= value_of_items.get(it)[1]
    else:
        points += value_of_items.get(it)[1]
        for i in range(value_of_items.get(it)[0]):
            bp.append(it)

for i in range(0, 9, 3):
    print('[{}], [{}], [{}]'.format(bp[i], bp[i+1], bp[i+2]))
print('\nИтоговые очки выживания: ' + str(points))

# _________________________________________________
#                   Доп. задание
''' Докажем, что нельзя получить положительный счёт, сложив предметы в 7 ячеек.
    Первое – берём ингалятор из-за условия(1, 5)
    Второе – берём максимально выгодные предметы снаибольшей ценностью и наименьшим местом("о": (1, 25),
                                                "н": (1, 15), "ф": (1, 15) – два предмета по 15 > один предмет по 20)
    Осталось 3 ячейки: берём "д": (1, 10) и "б": (2, 20). В любом случае в три ячейки больше, чем 30 очков получить нельзя.
    Итого: (5) + (25 + 15 + 15) + (10 + 20) = 90 очков
    Всего: 205
    Получается, взяв максимально выгодные предметы, получили отрицательный счёт. Следовательно нельзя сложить в 7 ячеек.
'''

