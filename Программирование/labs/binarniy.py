import pickle
import os
while True:
    print()
    print('='*25+' МЕНЮ '+25*'=')
    print('1) Создание новой базы данных')
    print('2) Открытие существующей базы данных')
    print('3) Просмотр всех записей в текущей базе данных')
    print('4) Добавление новой записи в базу данных')
    print('5) Поиск элементов по фильтру')
    print('6) Удаление по фильтру')
    print('0) Выход из программы')
    print(56*'=')
    a = input('Введите команду ')
    if a.isdigit()== False or int(a) > 6 or int(a) < 0:
        print('Введите корректную команду!')
    else:
        if a == '1':
            data = []
            f = input('Введите название новой базы данных: ')
            f = f+'.pickle'
            file = open(f,'wb')
            pickle.dump(data,file)
            file.close()
            print('Новая база данных '+f+' создана')
        if a == '2':
            print(os.listdir(path = os.getcwd())) 
            f = input('Введите имя базы данных, которую необходимо открыть: ')
        if a == '3':
            levo(text)
        if a =='4':
            pravo(text)
        if a == '5':
            shirina(text)
        if a == '6':
            kor_pred(text)
        if a == '7':
            words(text)
        if a == '0':
            break






















"""
import pickle
file_name = "ФИО.dat"
name = "Тихон"
age = 18
f = open(file_name, mode = 'w')
f.write('Hello!')
f.close()
"""

















