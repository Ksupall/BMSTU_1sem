import pickle
# ДОБАВЛЕНИЕ НОВОГО ЭЛЕМЕНТА
data = []
table =('\u250c'+'\u2500'*30+'\u252c'+('\u2500'*10+'\u252c')*3+
     '\u2500'*10+'\u2510\n\u2502'+' '*6+'НАЗВАНИЕ ПРОДУКТА'+
     ' '*7+'\u2502'+'   БЕЛКИ  '+'\u2502   ЖИРЫ   '+'\u2502'+
     ' УГЛЕВОДЫ '+'\u2502'+' КАЛОРИИ  '+'\u2502\n\u2514'+
     '\u2500'*30+'\u2534'+('\u2500'*10+'\u2534')*3+'\u2500'*10+'\u2518')
note = ['name','prot','fat','carb','kkal']
note[0] = input('Введите название продукта ')
note[1] = input('Введите кол-во белков: ')
note[2] = input('Введите кол-во жиров: ')
note[3] = input('Введите кол-во углеводов: ')
note[4] = input('Введите ко-во калорий: ')
data.append(note)
print(data)
f = open("Ksenya.pickle","wb")
pickle.dump(data,f)
f.close()
f = open("Ksenya.pickle","rb")
notel = len(pickle.load(f))
print(notel)
for i in range(notel):
    print(note[i])

         
"""
namel = len(name)
protl = len(str(prot))
fatl = len(str(fat))
carbl = len(str(carb))
kkall = len(str(kkal))
if namel > 30:
        name = name[:27]
        name = name+'...'
namel = len(name)
ad = (((32-namel)//2+(32-namel)%2)*' '+name+((32-namel)//2)*' '+
      ((11-protl)//2+(11-protl)%2)*' '+str(prot)+((11-protl)//2)*' '+
      ((10-fatl)//2+(10-fatl)%2)*' '+str(fat)+((10-fatl)//2)*' '+
      ((11-carbl)//2+(11-carbl)%2)*' '+str(carb)+((11-carbl)//2)*' '+
      ((11-kkall)//2+(11-kkall)%2)*' '+str(kkal)+((11-kkall)//2)*' ')
f = open("Ksenya.pickle","wb")
# ШАПКА ТАБЛИЦЫ
a = ('\u250c'+'\u2500'*30+'\u252c'+('\u2500'*10+'\u252c')*3+
     '\u2500'*10+'\u2510\n\u2502'+' '*6+'НАЗВАНИЕ ПРОДУКТА'+
     ' '*7+'\u2502'+'   БЕЛКИ  '+'\u2502   ЖИРЫ   '+'\u2502'+
     ' УГЛЕВОДЫ '+'\u2502'+' КАЛОРИИ  '+'\u2502\n\u2514'+
     '\u2500'*30+'\u2534'+('\u2500'*10+'\u2534')*3+'\u2500'*10+'\u2518')
pickle.dump(a,f)
# ЗАПИСИ В ТАБЛИЦЕ
f = open("Ksenya.pickle","wb")
b = (8*' '+'Гречневая каша'+14*' '+'4.5'+7*' '+'1.6'+8*' '+'27.4'+
     7*' '+'137\n  Колбаса вареная Докторская  ' +5*' '+'13.4'+6*' '+
     '22.9'+11*' '+'0'+7*' '+'257\n'+10*' '+'Кефир 2,5%'+18*' '+
     '3'+7*' '+'2.5'+11*' '+'4'+8*' '+'51\n'+11*' '+'Говядина'+16*' '+'18.7'+
     6*' '+'12.6'+11*' '+'0'+7*' '+'191\n'+11*' '+'Индейка'+17*' '+
     '21.1'+6*' '+'12.3'+11*' '+'0'+7*' '+'192\n'+12*' '+'Шпинат'+
     18*' '+'2.5'+9*' '+'0'+9*' '+'2.6'+8*' '+'22\n'+12*' '+'Фундук'+
     17*' '+'16.3'+6*' '+'66.7'+9*' '+'9.8'+7*' '+'701\n'+9*' '+
     'Окунь морской'+13*' '+'17.4'+7*' '+'5.5'+11*' '+'0'+7*' '+'123\n'+
     9*' '+'Яйцо куриное'+14*' '+'12.9'+6*' '+'11.1'+9*' '+'0.6'+7*' '+'153\n'+
     7*' '+'Яйцо перепелиное'+12*' '+'11.9'+6*' '+'13.3'+9*' '+'0.9'+
     7*' '+'170\n')
b += ad
pickle.dump(b,f)
f = open("Ksenya.pickle","rb")
pickle.load(f)
print(a)
print(b)
f.close()
print()
print('ПОИСК ЭЛЕМЕНТОВ ПО:')
print('1 - названию')
print('2 - кол-ву белков')
print('3 - кол-ву жиров')
print('4 - кол-ву углеводов')
p = int(input('Введите команду: '))
НЕ ЗНАЮ, КАК ЭТО ДЕЛАТЬ((((
if p == 1:
        n = input('Введите название: ')
        f = open("Ksenya.pickle","rb")
        q = pickle.load(f)
        print(q)



prott = prot
protg = True
for i in prott:
        l = 0
        if prott[0] == '-':
                protg = False
        r = prott.find('.')
        if r != -1:
                prott = prott[:r]+prott[(r+1):]   
        if not prott.isdigit():
                protg = False

fatt = fat
fatg = True
for i in fatt:
        l = 0
        if fatt[0] == '-':
                fatg = False
        r = fatt.find('.')
        if r != -1:
                fatt = fatt[:r]+fatt[(r+1):]   
        if not fatt.isdigit():
                fatg = False















        
"""           































      
