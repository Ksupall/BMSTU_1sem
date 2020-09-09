
"""
n-начальное значение
k-конечное значение
sh-шаг
"""
from math import exp
n = float(input('Введите начальное значение '))
k = float(input('Введите конечное значение '))
sh = float(input('Введите шаг '))
print('   N     \u2502       q        \u2502'
      +'         '+'x\u2081     \u2502        x\u2082')
print (37*'\u2501')
w = 0
eps = 1e-7
l = abs((k-n)/sh) + eps
N = 0
q = n
x1min = 2.97*(n**4) + 4.84*(n**3) - 16.4*n*n + 41.2*n - 33.2
x1max = 2.97*(n**4) + 4.84*(n**3) - 16.4*n*n + 41.2*n - 33.2
while N < l:
    x1 = 2.97*(q**4) + 4.84*(q**3) - 16.4*q*q + 41.2*q - 33.2
    x2 = 2 - (q*(exp(q)))
    if ( x1 > 1000 or x2 > 1000):
        print('{:8d}'.format(N+1),'\u2502',
                '{:14.4f}'.format(q),'\u2502',
                '{:14.4e}'.format(x1),'\u2502',     
                '{:14.4e}'.format(x2))
    elif (x1 <1000 and x2 < 1000):
         print ('{:8d}'.format(N+1),'\u2502',
                '{:14.4f}'.format(q),'\u2502',
                '{:14.4f}'.format(x1),'\u2502',     
                '{:14.4f}'.format(x2))

    if x1 > x1max:
        x1max = x1
    if x1 < x1min:
        x1min = x1
    q = q + sh
    N = N + 1

print(42*'\u2501')
print(25*' '+'Построение графика ')
print(42*'\u2501')
print()
print()
dl = 6
kol = 10
if N > 1:
    vse = dl*kol
    if (x1max < 0) or (x1min > 0):
        o = vse+1
    else:
        o = round((0 - x1min)/(x1max - x1min)*vse)
    pd = (x1max-x1min)/dl
    m = 10000
else:
    kol = 2
    vse = dl*kol
    o = dl
if o > vse:
    qc = x1min
else:
    qc = -o/kol*pd
print(' ', end='')
w = 0
while w <= vse:
    if o <= vse:
        if abs(w - o)%kol == 0:
            if w == o:
                print ('        0', end='')
            else:
                print(' {:9.2e}'.format(qc),end='') 
            qc += pd
            w += kol
        else:
            print(' ',end='')
            w += 1
    else:
         if qc >= 1000:
            print(' {:9.2e}'.format(qc),end='')
         elif qc < 1000:
             print(' {:9.2f}'.format(qc),end='')
    qc += pd
    w += kol
print('\n',7*' ','q ',sep = '', end = '')

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
print(' x1')
w = n
while w < k + sh :
    x1 = 2.97*(w**4) + 4.84*(w**3) - 16.4*w*w + 41.2*w - 33.2
    print('{:8.3f}'.format(w),end = '')
    w += sh
    p = round(((x1-x1min) / (x1max-x1min) * vse))
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






































            
