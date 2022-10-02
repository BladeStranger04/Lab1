import csv
import os


def paint(code):
    return f'\u001b[{code}m'


end = paint(0)
red = paint(41)
yellow = paint(43)
green = paint(42)
white = paint(47)
black = paint(40)

# ------------------> Task 1 <--------------------
# for i in range(3):
#     print(green + '   ' * 4 + red + '   ' * 6 + end)
# for i in range(3):
#     print(green + '   ' * 4 + yellow + '   ' * 6 + end)


# ------------------> Task 2 <--------------------
sqr = red + ' ' * 3  # красный квадрат
sqe = end + ' ' * 3  # пустой квадрат

# print((sqe * 4 + sqr * 1 + sqe * 3) * 4 + end)
# for i in range(3):
#     print((sqe * 3 + sqr * 3 + sqe * 2) * 4 + end)
#     print((sqe * 2 + sqr * 5 + sqe * 1) * 4 + end)
#     print((sqe * 1 + sqr * 7 + sqe * 0) * 4 + end)
#
#     print(sqe * 0 + sqr * 33 + end)
#
#     print((sqe * 1 + sqr * 7 + sqe * 0) * 4 + end)
#     print((sqe * 2 + sqr * 5 + sqe * 1) * 4 + end)
#     print((sqe * 3 + sqr * 3 + sqe * 2) * 4 + end)
#     print((sqe * 4 + sqr * 1 + sqe * 3) * 4 + end)


# ------------------> Task 3 <--------------------

#
# # генерация таблицы
# size = 11
# matrix = [[0 for i in range(size)] for j in range(size)]
# for i in range(size):
#     for j in range(size):
#         if j == 0:
#             matrix[i][j] = size - i - 1
#         if i == size - 1:
#             matrix[i][j] = j
#
# # изменяем массив под функцию
# for x in range(1, size):
#     if 0 <= size - x - 2 <= size:
#         matrix[size - x - 2][x] = '/'
#
# # отрисовываем массив
# for i in range(size-1):
#     line = ''
#     for j in range(size):
#         if matrix[i][j] == '/':
#             line += white + '  ' + black
#         elif matrix[i][j] == 0:
#             line += black + '  '
#         else:
#             line += black + str(matrix[i][j]) + ' '
#     print(line)
# print(black + '0 1 2 3 4 5 6 7 8 9 10')

# ------------------> Task 4 <--------------------
# нахождение процента книг
# more_150 = 0
# less_150 = 0
# with open('books.csv') as csvfile:
#     table = list(csv.reader(csvfile, delimiter=';'))[1:]
#     for book in table:
#         if float(book[7].replace(',', '.')) > 150:
#             more_150 += 1
#         else:
#             less_150 += 1
# all = more_150 + less_150
# percent_more_150 = round(more_150 / all * 100)
# percent_less_150 = round(less_150 / all * 100)
#
# # отрисовка диаграммы с анимацией
# print(black + ' 100% |' + black)
# print(black + '      |' + black)
# print(black + '  90% |' + black)
# print(black + '      |' + black)
# print(black + '  80% |' + black)
# print(black + '      |' + black)
# print(black + '  70% |' + ' ' * 12 + white + '    ' + black)
# print(black + '      |' + ' ' * 12 + white + '    ' + black)
# print(black + '  60% |' + ' ' * 12 + white + '    ' + black)
# print(black + '      |' + ' ' * 12 + white + '    ' + black)
# print(black + '  50% |' + ' ' * 12 + white + '    ' + black)
# print(black + '      |' + ' ' * 12 + white + '    ' + black)
# print(black + '  40% |' + ' ' * 12 + white + '    ' + black)
# print(black + '      |' + ' ' * 12 + white + '    ' + black)
# print(black + '  30% |' + ' ' * 12 + white + '    ' + black + ' ' * 12 + white + '    ' + black)
# print(black + '      |' + ' ' * 12 + white + '    ' + black + ' ' * 12 + white + '    ' + black)
# print(black + '  20% |' + ' ' * 12 + white + '    ' + black + ' ' * 12 + white + '    ' + black)
# print(black + '      |' + ' ' * 12 + white + '    ' + black + ' ' * 12 + white + '    ' + black)
# print(black + '  10% |' + ' ' * 12 + white + '    ' + black + ' ' * 12 + white + '    ' + black)
# print(black + '       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
# print(black + '                   >150           <=150')

