from math import cos
n = float(input('Введите начальное значение: '))
k = float(input('Введите конечное значение: '))
sh = float(input('Введите шаг: '))
eps = 1e-7
l = abs((k-n)/sh) + eps
ymin = 10000
ymax = -10000
x = n
N = 0
while N < l:
    y = cos(x)**2/x**3-2*x
    if y > ymax:
        ymax = y
    if y < ymin:
        ymin = y
    x += sh
    N += 1
dl = 6
kol = 10

if N > l:
    vse = dl*kol
    if (ymax < 0) or (ymin > 0):
        o = vse+1
    else:
        o = round((0 - ymin)/(ymax - ymin)*vse)
    pd = (ymax - ymin)/dl
else:
    kol = 2
    vse = dl*kol
    o = dl
if o > vse:
    yc = ymin
else:
    yc = -o/kol*pd
print(' ', end='')
w = 0
while w <= vse:
    if o <= vse:
        if abs(w - o)%kol == 0:
            if w == o:
                print ('        0', end='')
            else:
                if yc >= 1000:
                    print(' {:9.2e}'.format(yc),end='')
                else:
                    print(' {:9.2f}'.format(yc),end='')
            yc += pd
            w += kol
        else:
            print(' ',end='')
            w += 1
    else:
         if yc >= 1000:
            print(' {:9.2e}'.format(yc),end='')
         else:
            print(' {:9.2f}'.format(yc),end='')
         yc += pd
         w += kol
print('\n',7*' ','x ',sep = '', end = '')

w = 0
while w <= vse:
    if o <= vse:
        if w == o:
            print ('\u253c',end = '')
        elif abs(w - o)%kol == 0:
            print ('\u2534',end = '')
        else:
            print ('\u2500',end = '')
    else:
        if abs(w)%kol == 0:
            print ('\u2534',end = '')
        else:
            print ('\u2500',end = '')
    w +=1
print(' y')
w = 0
x = n
while w < N :
    y = cos(x)**2/x**3-2*x
    print('{:8.3f}'.format(x),end = '')
    w += 1
    x += sh
    p = round(((y-ymin) / (ymax-ymin) * vse))
    if o <= vse:
        if p <= o:
            print(p*' ','*',end = '')
            if (p < o) and (o <= vse):
                print((o-1-p)*' ','\u2502',sep = '',end = '')
        else:
            print((o+1)*' ','\u2502',(p-o-1)*' ','*',sep = '',end = '')
    else:
        print(p*' ','*',end = '')
    print()







































          









































































































"""



"""
