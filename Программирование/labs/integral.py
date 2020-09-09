am = False
bm = False
a = input('Введите a: ')
b = input('Введите b: ')
for i in a:
    l = 0
    if i[0] == '-':
        i = i[1::1]
    r = i.find('.')
    if r != -1:
        i = i[:r]+i[(r+1):]
    r = i.find('e+')
    if r != -1:
        i = i[:r]+i[(r+2):]
    else:
        r = i.find('e-')
        if r != -1:
            i = i[:r]+i[(r+2):]   
    if not i.isdigit():
        am = False
    else:
        am = True
for i in b:
    l = 0
    if i[0] == '-':
        i = i[1::1]
    r = i.find('.')
    if r != -1:
        i = i[:r]+i[(r+1):]
    r = i.find('e+')
    if r != -1:
        i = i[:r]+i[(r+2):]
    else:
        r = i.find('e-')
        if r != -1:
            i = i[:r]+i[(r+2):]   
    if not i.isdigit():
        bm = False
    else:
        bm = True
if am == False or bm == False
    print('Введите корректные значения!')
if bm == True and am == True:
    n = input('Введте число n: ')
    nm = False
    for i in b:
    l = 0
    if i[0] == '-':
        i = i[1::1]
    r = i.find('.')
    if r != -1:
        i = i[:r]+i[(r+1):]
    r = i.find('e+')
    if r != -1:
        i = i[:r]+i[(r+2):]
    else:
        r = i.find('e-')
        if r != -1:
            i = i[:r]+i[(r+2):]   
    if not i.isdigit():
        bm = False
    else:
        bm = True
    if nm == False:
        print('Введитк корректное число n!')
    else:
        h = (b-a)//n



        
