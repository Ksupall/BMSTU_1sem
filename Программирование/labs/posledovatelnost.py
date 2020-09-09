from math import factorial
x = float(input('Введите x: '))
Nmax = int(input('Введите максимальное значение n: '))
step = int(input('Введите шаг: '))
eps = float(input('Введите eps: '))
print('   N     \u2502       x        \u2502'
      +'       '+'n      \u2502       S')
print (35*'\u2501')
n = 1
s = 0
N = 1
t = x**n/factorial(n)
while  n < Nmax:
    t = x**n/factorial(n)
    s += t
    if ( t > 1000 or x > 1000):
        print('{:8d}'.format(N),'\u2502',
                '{:14.4e}'.format(x),'\u2502',
                '{:14d}'.format(n),'\u2502',     
                '{:14.4e}'.format(s+1 ))
    elif (t <1000 and s < 1000):
         print ('{:8d}'.format(N),'\u2502',
                '{:14.4f}'.format(n),'\u2502',
                '{:14d}'.format(n),'\u2502',     
                '{:14.4f}'.format(s+1))
    N += 1
    n += 1

