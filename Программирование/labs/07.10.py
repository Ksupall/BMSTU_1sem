
"""
n-начальное значение
k-конечное значение
sh-шаг
"""
from math import exp
n = float(input('Введите начальное значение '))
k = float(input('Введите конечное значение '))
sh = float(input('Введите шаг '))
print('      \u004e     \u2502     \u0071        \u2502'
      +'         '+'\u0078\u2081         \u2502        \u0078\u2082')
print (41*'\u2501')
w = 0
eps = 1e-7
l = abs((k-n)/sh) + eps
N = 1
q = n
x1min = 2.97*(n**4) + 4.84*(n**3) - 16.4*n*n + 41.2*n - 33.2
x1max = 2.97*(n**4) + 4.84*(n**3) - 16.4*n*n + 41.2*n - 33.2
while q <= k + sh:
    x1 = 2.97*(q**4) + 4.84*(q**3) - 16.4*q*q + 41.2*q - 33.2
    x2 = 2 - (q*(exp(q)))
    print ('   ','{:3.0f}'.format(N).rjust(2),'    \u2502',
            '{:.4f}'.format(q).rjust(8),'    \u2502',
            '{:14.4e}'.format(x1).rjust(6),'    \u2502',
            '{:14.4e}'.format(x2).rjust(6))
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
if l > 1:
    dl = 6
    kol = 10
    vse = dl*kol
    print (' ', end='')
    if (x1max < 0) or (x1min > 0):
        o = vse+1
    else:
        o =int((0 - x1min)/(x1max - x1min)*vse)
    pd = (x1max-x1min)/dl
    m = 10000
if o > vse:
    qc = x1min
else:
    qc = -o/kol*pd
w = 0
while w <= vse:
    if o <= vse:
        if abs(w - o)%kol == 0:
            if w == o:
                print ('     0', end='')
            print('  {:9.2e}'.format(qc),end='')
            qc += pd
            w += kol
        else:
            print(' ',end='')
            w += 1
    else:
        print(' {:9.2e}'.format(qc),end='')
        qc += pd
        w += kol
print('\n',7*' ','x1 ',sep = '', end = '')

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
print (' q')
w = n
while w < k + sh :
    x1 = 2.97*(w**4) + 4.84*(w**3) - 16.4*w*w + 41.2*w - 33.2
    print('{:8.3f}'.format(x1),end = '')
    print()
    w += sh
    p = round(((x1-x1min) / (x1max-x1min) * vse))
    if p <= o:
        print (p*' ','*',end = '')
        if (p < o) and (o <= vse):
            print((o-1-p)*' ','\u2502',sep = '',end = '')
    else:
        print((o+1)*' ','\u2502',(p-o-1)*' ',sep = '',end = '')

"""

if x1 > x1max:
        x1max = x1
    if x1 < x1min:
        x1min = x1


if (x1 < 1000 or x2 < 1000):
        print ('   ','{:3.0f}'.format(N).rjust(2),'   \u2502', 
              '{:.4f}'.format(q).rjust(8),'     \u2502',
              '{:.4f}'.format(x1).rjust(10),'    \u2502',
              '{:.4f}'.format(x2).rjust(8))
    
if abs(qc) < 10000:
            print(' {:9.2f}'.format(qc),end='')


if abs(qc) < 1000:
                print (' {:9.2f}'.format(qc),end='')
            if abs(qc) > 1000:







"""





































            
