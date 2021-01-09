import pickle

file = 'backup.data'
pb = {}


def total():
    print('\n----------PHONEBOOK-----------')
    for j, k in pb.items():
        print(f'Имя: {j} Телефон: {k}')
    print('------------------------------\n')


def plus(a, b):
    pb[a] = b
    print(f'Добавлен {a}')


def minus(a):
    if a in pb:
        del pb[a]
        print(f'Удален {a}')
    else:
        print(f'Контакта {a} нет')


def search(a):
    if a in pb:
        print(f'Вы искали {a}, есть такой контакт, его номер {pb[a]}')
    else:
        print(f'Вы искали {a}, нет такого контакта')


def save():
    global pb
    f = open(file, 'wb')
    pickle.dump(pb, f)  # помещаем объект в файл
    print('\nСохранение прошло успешно')
    f.close()


def load():
    global pb
    f = open(file, 'rb')
    pb = pickle.load(f)  # загружаем объект из файла
    print('\nЗагрузка прошла успешно')
    f.close()


while True:
    i = input(
        '-----------------------------\n1 - Просмотр телефонной книги\n2 - Поиск контакта\n3 - Добавление \
контакта\n4 - Изменение контакта\n5 - Удаление контакта\n6 - Сохранить телефонную книгу\n7 - Загрузить \
телефонную книгу\n0 - Выход из программы\n-----------------------------\nВведите номер:')
    if i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '0':
        print('Вы ввели что-то не потребное')
    elif int(i) == 1:
        total()
    elif int(i) == 2:
        search(input('Введи имя:'))
    elif int(i) == 3:
        plus((input('Введи имя:')), int(input('Введи номер:')))
    elif int(i) == 4:
        plus((input('Введи имя:')), int(input('Введи номер:')))
    elif int(i) == 5:
        minus(input('Введи имя:'))
    elif int(i) == 6:
        save()
    elif int(i) == 7:
        load()
    elif int(i) == 0:
        break
