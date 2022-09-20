import csv

with open('books.csv') as csvfile:
    table = list(csv.reader(csvfile, delimiter=';'))[1:]

    '''# ___________________Task №1________________________

    print(len(table))

    # ___________________Task №2________________________

    c = 0
    for rec in table:
        if len(rec[1]) > 30:
            c += 1
    print(c)

    # ___________________Task №3________________________

    # Создаём массив записей, удовлетворяющий ограничениям:
    mas = []
    for rec in table:
        if rec[6][6:10] == '2015' or rec[6][6:10] == '2018':
            mas.append(rec)

    # Функция по поиску книг по автору

    def search(name):
        books = []
        for rec in mas:
            if name in rec[3]:
                books.append(rec[1])
        return books

    need = input()
    while need != 'Стоп':
        print('\n'.join(search(need)))
        need = input()

    # ___________________Task №4________________________
    f = open('Task4', 'w')
    for i in range(1, 21):
        s = f'{i}). {table[i][3]}. {table[i][1]} - {table[i][6][6:10]}\n'
        f.write(s)

    # ___________________Extra №1________________________
    tags = set()
    for rec in table:
        tag = rec[-1].replace('# ', ' ##').split(' #')
        for i in tag:
            tags.add(i)
    print('\n'.join(tags))

    # ___________________Extra №2________________________
    # создал массив кол-ва всех выдач книг
    mas_sold = []
    for rec in table:
        mas_sold.append(int(rec[8]))
    
    # перебираем все книги, которые удовлетворяют максимальному кол-ву выдач.
    # сделал доп массив, чтобы не было повторений в выведенном списке.
    
    c = 1
    maxi = max(mas_sold)
    copies = []
    print('Топ 20 самых популярных книг:\n')
    for i in range(len(mas_sold)):
        if c == 21:
            break
        if mas_sold[i] == maxi:
            if table[i][1] not in copies:
                print(f'{c}). {table[i][1]}')
                c += 1
                copies.append(table[i][1])'''
