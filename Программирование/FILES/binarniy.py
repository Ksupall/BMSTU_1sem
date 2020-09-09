import pickle
import os
data = [['Гречневая каша','4.5','1.6','27.4','137'],['Колбаса вареная Докторская','13.4',
             '22.9','0','257'],['Кефир 2,5%','3','2.5','4','51'],['Говядина','18.7','12.6','0','191'],
            ['Индейка','21.1','12.3','0','192'],['Шпинат','2.5','0','2.6','22'],['Фундук','16.3','66.7','9.8','701'],
            ['Окунь морской','17.4','5.5','0','123'],['Яйцо куриное','12.9','11.1','0.6','153'],
            ['Яйцо перепелиное','11.9','13.3','0.9','170']]
while True:
    print()
    print('='*25+' МЕНЮ '+25*'=')
    print('1) Создание новой базы данных')
    print('2) Открытие существующей базы данных')
    print('3) Просмотр всех записей в текущей базе данных')
    print('4) Добавление новой записи в базу данных')
    print('5) Поиск элементов по фильтру')
    print('6) Удаление по фильтру')
    print('7) Сохранить базу данных')
    print('0) Выход из программы')
    print(56*'=')
    a = input('Введите команду ')
    if a.isdigit()== False or int(a) > 7 or int(a) < 0:
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
            po = []
            print('Все базы данных: ')
            p = os.listdir(path = os.getcwd())
            for i in range(len(p)):
                pl = len(p[i])
                if p[i][pl-7:] == '.pickle':
                    po.append(p[i][:pl-7])
                    print(p[i][:pl-7])
            while True:
                if po == []:
                    print('Баз данных нет!')
                    break
                else:
                    f = input('Введите имя базы данных, которую необходимо открыть: ')
                    if f in po:
                        f = f+'.pickle'
                        file = open(f,'rb')
                        data = pickle.load(file)
                        file.close()
                        print('База данных ',f,'открыта')
                        break
                    else:
                        print('Такой базы данных нет!')
        if a == '3':
            print('\u250c'+'\u2500'*30+'\u252c'+('\u2500'*10+'\u252c')*3+
             '\u2500'*10+'\u2510\n\u2502'+' '*6+'НАЗВАНИЕ ПРОДУКТА'+
             ' '*7+'\u2502'+'   БЕЛКИ  '+'\u2502   ЖИРЫ   '+'\u2502'+
             ' УГЛЕВОДЫ '+'\u2502'+' КАЛОРИИ  '+'\u2502\n\u2514'+
             '\u2500'*30+'\u2534'+('\u2500'*10+'\u2534')*3+'\u2500'*10+'\u2518')
            for i in range(len(data)):
                print(((32-len(data[i][0]))//2+(32-len(data[i][0]))%2)*' '+data[i][0]+((32-len(data[i][0]))//2)*' '+
                ((11-len(data[i][1]))//2+(11-len(data[i][1]))%2)*' '+data[i][1]+((11-len(data[i][1]))//2)*' '+
                ((10-len(data[i][2]))//2+(10-len(data[i][2]))%2)*' '+data[i][2]+((10-len(data[i][2]))//2)*' '+
                ((11-len(data[i][3]))//2+(11-len(data[i][3]))%2)*' '+data[i][3]+((11-len(data[i][3]))//2)*' '+
                ((11-len(data[i][4]))//2+(11-len(data[i][4]))%2)*' '+data[i][4]+((11-len(data[i][4]))//2)*' ')                
        if a =='4':
            note = [0,0,0,0,0]
            note[0] = input('Введите название продукта: ')
            if len(note[0]) > 30:
                note[0] = note[0][:27]
                note[0] = note[0]+'...'
            while True:
                note[1] = input('Введите кол-во белков: ')
                note1 = note[1]
                o = True
                note[2] = input('Введите кол-во жиров: ')
                note2 = note[2]
                u = True
                note[3] = input('Введите кол-во углеводов: ')
                note3 = note[3]
                y = True
                note[4] = input('Введите кол-во калорий: ')
                note4 = note[4]
                s = True
                for i in note1:
                    l = 0
                    if note1[0] == '-':
                            o = False
                    r = note1.find('.')
                    if r != -1:
                            note1 = note1[:r]+note[1][(r+1):]   
                    if not note1.isdigit():
                            o = False
                for i in note2:
                    l = 0
                    if note2[0] == '-':
                            u = False
                    r = note2.find('.')
                    
                    if r != -1:
                            note2 = note2[:r]+note2[(r+1):]   
                    if not note2.isdigit():
                            u = False
                for i in note3:
                    l = 0
                    if note3[0] == '-':
                            y = False
                    r = note3.find('.')
                    if r != -1:
                            note3 = note3[:r]+note3[(r+1):]   
                    if not note3.isdigit():
                            y = False
                for i in note4:
                    l = 0
                    if note4[0] == '-':
                            s = False
                    r = note4.find('.')
                    if r != -1:
                            note4 = note4[:r]+note4[(r+1):]   
                    if not note4.isdigit():
                            s = False
                if o == False or u == False or y == False or s == False:
                    print('Данные введены неверно!')
                else:
                    break
            data.append(note)
            print('\u250c'+'\u2500'*30+'\u252c'+('\u2500'*10+'\u252c')*3+
                 '\u2500'*10+'\u2510\n\u2502'+' '*6+'НАЗВАНИЕ ПРОДУКТА'+
                 ' '*7+'\u2502'+'   БЕЛКИ  '+'\u2502   ЖИРЫ   '+'\u2502'+
                 ' УГЛЕВОДЫ '+'\u2502'+' КАЛОРИИ  '+'\u2502\n\u2514'+
                 '\u2500'*30+'\u2534'+('\u2500'*10+'\u2534')*3+'\u2500'*10+'\u2518')
            for i in range(len(data)):
                print(((32-len(data[i][0]))//2+(32-len(data[i][0]))%2)*' '+data[i][0]+((32-len(data[i][0]))//2)*' '+
                ((11-len(data[i][1]))//2+(11-len(data[i][1]))%2)*' '+data[i][1]+((11-len(data[i][1]))//2)*' '+
                ((10-len(data[i][2]))//2+(10-len(data[i][2]))%2)*' '+data[i][2]+((10-len(data[i][2]))//2)*' '+
                ((11-len(data[i][3]))//2+(11-len(data[i][3]))%2)*' '+data[i][3]+((11-len(data[i][3]))//2)*' '+
                ((11-len(data[i][4]))//2+(11-len(data[i][4]))%2)*' '+data[i][4]+((11-len(data[i][4]))//2)*' ')
        if a == '5':
            data_new = []
            note_new = [0,0,0,0,0]
            print('ПОИСК ЭЛЕМЕНТОВ ПО:\n1 - названию\n2 - кол-ву белков\n3 - кол-ву жиров\n'+
                  '4 - кол-ву углеводов\n5 - по кол-ву калорий')
            while True:
                poisk = input('Команда: ')
                if (poisk == '1' or poisk == '2' or poisk == '3' or
                    poisk == '4' or poisk == '5'):
                    break
                else:
                    print('Введите корректную команду!')
            # ПОИСК ПО НАЗВАНИЮ
            if poisk == '1':
                print('1 - полное название\n2 - часть названия')
                while True:
                    poiskn = input('Команда: ')
                    if poiskn == '1' or poiskn == '2':
                        break
                    else:
                        print('Введите корректную команду!')
                if poiskn == '1':
                    poisk_name = input('Введите название, которое необходимо найти: ')
                    for i in range(len(data)):
                        if data[i][0] == poisk_name:
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
                if poiskn == '2':
                    poisk_name = input('Введите название, которое необходимо найти: ')
                    for i in range(len(data)):
                        r = data[i][0].find(poisk_name)
                        if r == 0:
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
            # ПОИСК ПО КОЛ-ВУ БЕЛКОВ
            if poisk == '2':
                print('1 - больше a\n2 - меньше a\n3 - равно a')
                while True:
                    poiskn = input('Команда: ')
                    if poiskn == '1' or poiskn == '2' or poiskn == '3':
                        break
                    else:
                        print('Введите корректную команду!')
                if poiskn == '1':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][1]) > float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
                if poiskn == '2':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][1]) < float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
                if poiskn == '3':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][1]) == float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
            # ПОИСК ПО КОЛ-ВУ ЖИРОВ
            if poisk == '3':
                print('1 - больше a\n2 - меньше a\n3 - равно a')
                while True:
                    poiskn = input('Команда: ')
                    if poiskn == '1' or poiskn == '2' or poiskn == '3':
                        break
                    else:
                        print('Введите корректную команду!')
                if poiskn == '1':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][2]) > float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
                if poiskn == '2':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][2]) < float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
                if poiskn == '3':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][2]) == float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
            # ПОИСК ПО КОЛ-ВУ УГЛЕВОДОВ
            if poisk == '4':
                print('1 - больше a\n2 - меньше a\n3 - равно a')
                while True:
                    poiskn = input('Команда: ')
                    if poiskn == '1' or poiskn == '2' or poiskn == '3':
                        break
                    else:
                        print('Введите корректную команду!')
                if poiskn == '1':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][3]) > float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
                if poiskn == '2':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][3]) < float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
                if poiskn == '3':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][3]) == float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
            # ПОИСК ПО КАЛОРИЯМ
            if poisk == '5':
                print('1 - больше a\n2 - меньше a\n3 - равно a')
                while True:
                    poiskn = input('Команда: ')
                    if poiskn == '1' or poiskn == '2' or poiskn == '3':
                        break
                    else:
                        print('Введите корректную команду!')
                if poiskn == '1':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][4]) > float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
                if poiskn == '2':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][4]) < float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
                if poiskn == '3':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][4]) == float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                            data_new.append(note_new)
            print('\u250c'+'\u2500'*30+'\u252c'+('\u2500'*10+'\u252c')*3+
     '\u2500'*10+'\u2510\n\u2502'+' '*6+'НАЗВАНИЕ ПРОДУКТА'+
     ' '*7+'\u2502'+'   БЕЛКИ  '+'\u2502   ЖИРЫ   '+'\u2502'+
     ' УГЛЕВОДЫ '+'\u2502'+' КАЛОРИИ  '+'\u2502\n\u2514'+
     '\u2500'*30+'\u2534'+('\u2500'*10+'\u2534')*3+'\u2500'*10+'\u2518')
            for i in range(len(data_new)):
                print(((32-len(data_new[i][0]))//2+(32-len(data_new[i][0]))%2)*' '+str(data_new[i][0])+((32-len(data_new[i][0]))//2)*' '+
                ((11-len(data_new[i][1]))//2+(11-len(data_new[i][1]))%2)*' '+str(data_new[i][1])+((11-len(data_new[i][1]))//2)*' '+
                ((10-len(data_new[i][2]))//2+(10-len(data_new[i][2]))%2)*' '+str(data_new[i][2])+((10-len(data_new[i][2]))//2)*' '+
                ((11-len(data_new[i][3]))//2+(11-len(data_new[i][3]))%2)*' '+str(data_new[i][3])+((11-len(data_new[i][3]))//2)*' '+
                ((11-len(data_new[i][4]))//2+(11-len(data_new[i][4]))%2)*' '+str(data_new[i][4])+((11-len(data_new[i][4]))//2)*' ')
        if a == '6':
            data_new = data
            note_new = [0,0,0,0,0]
            print('УДАЛИТЬ ЭЛЕМЕНТ ПО:\n1 - названию\n2 - кол-ву белков\n3 - кол-ву жиров\n'+
                  '4 - кол-ву углеводов\n5 - по кол-ву калорий')
            while True:
                poisk = input('Команда: ')
                if (poisk == '1' or poisk == '2' or poisk == '3' or
                    poisk == '4' or poisk == '5'):
                    break
                else:
                    print('Введите корректную команду!')
            # ПОИСК ПО НАЗВАНИЮ
            if poisk == '1':
                print('1 - полное название\n2 - часть названия')
                while True:
                    poiskn = input('Команда: ')
                    if poiskn == '1' or poiskn == '2':
                        break
                    else:
                        print('Введите корректную команду!')
                if poiskn == '1':
                    poisk_name = input('Введите название, которое необходимо удалить: ')
                    for i in range(len(data)):
                        if data[i][0] == poisk_name:
                            note_new[0] = ''
                            note_new[1] = ''
                            note_new[2] = ''
                            note_new[3] = ''
                            note_new[4] = ''
                    data_new.append(note_new)
                if poiskn == '2':
                    poisk_name = input('Введите название, которое необходимо найти: ')
                    for i in range(len(data)):
                        r = data[i][0].find(poisk_name)
                        if r == 0:
                            note_new[0] = ''
                            note_new[1] = ''
                            note_new[2] = ''
                            note_new[3] = ''
                            note_new[4] = ''
                            data_new.append(note_new)
            # ПОИСК ПО КОЛ-ВУ БЕЛКОВ
            if poisk == '2':
                print('1 - больше a\n2 - меньше a\n3 - равно a')
                while True:
                    poiskn = input('Команда: ')
                    if poiskn == '1' or poiskn == '2' or poiskn == '3':
                        break
                    else:
                        print('Введите корректную команду!')
                if poiskn == '1':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][1]) > float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                    data_new.append(note_new)
                if poiskn == '2':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][1]) < float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                    data_new.append(note_new)
                if poiskn == '3':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][1]) == float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                    data_new.append(note_new)
            # ПОИСК ПО КОЛ-ВУ ЖИРОВ
            if poisk == '3':
                print('1 - больше a\n2 - меньше a\n3 - равно a')
                while True:
                    poiskn = input('Команда: ')
                    if poiskn == '1' or poiskn == '2' or poiskn == '3':
                        break
                    else:
                        print('Введите корректную команду!')
                if poiskn == '1':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][2]) > float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                    data_new.append(note_new)
                if poiskn == '2':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][2]) < float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                    data_new.append(note_new)
                if poiskn == '3':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][2]) == float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                    data_new.append(note_new)
            # ПОИСК ПО КОЛ-ВУ УГЛЕВОДОВ
            if poisk == '4':
                print('1 - больше a\n2 - меньше a\n3 - равно a')
                while True:
                    poiskn = input('Команда: ')
                    if poiskn == '1' or poiskn == '2' or poiskn == '3':
                        break
                    else:
                        print('Введите корректную команду!')
                if poiskn == '1':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][3]) > float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                    data_new.append(note_new)
                if poiskn == '2':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][3]) < float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                    data_new.append(note_new)
                if poiskn == '3':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][3]) == float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                    data_new.append(note_new)
            # ПОИСК ПО КАЛОРИЯМ
            if poisk == '5':
                print('1 - больше a\n2 - меньше a\n3 - равно a')
                while True:
                    poiskn = input('Команда: ')
                    if poiskn == '1' or poiskn == '2' or poiskn == '3':
                        break
                    else:
                        print('Введите корректную команду!')
                if poiskn == '1':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][4]) > float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                    data_new.append(note_new)
                if poiskn == '2':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][4]) < float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                    data_new.append(note_new)
                if poiskn == '3':
                    while True:
                        kol = input('Введите количество: ')
                        koll = True
                        for i in kol:
                            l = 0
                            if kol[0] == '-':
                                    koll = False
                            r = kol.find('.')
                            if r != -1:
                                    kol = kol[:r]+kol[(r+1):]   
                            if not kol.isdigit():
                                    koll = False
                        if koll == False:
                            print('Введите корректное количество!')
                        else:
                            break
                    for i in range(len(data)):
                        if float(data[i][4]) == float(kol):
                            note_new[0] = data[i][0]
                            note_new[1] = data[i][1]
                            note_new[2] = data[i][2]
                            note_new[3] = data[i][3]
                            note_new[4] = data[i][4]
                    data_new.append(note_new)
        if a == '7':
            file = open(f,'wb')
            pickle.dump(data,file)
            file.close()
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

















