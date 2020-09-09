from math import factorial
x = float(input('Введите число x: '))
Kmax = int(input('Введите максимальное число n: '))
step = float(input('Введите шаг: '))
eps = float(input('Введите eps: '))
print('   N     \u2502       x        \u2502'
    +'       '+'r       \u2502      S')
print (36*'\u2501')
n = 1
s = 0
K = 1
r = x**n/n
Nstep=1
while K <= Kmax and abs(r) > eps:
    r = x**n/n
    s += r
    if K == Nstep:
        if (r > 10000000 and x < 10000):
            print('{:8d}'.format(K),'\u2502',
                    '{:14.4f}'.format(x),'\u2502',
                    '{:13.4f}'.format(r),'\u2502',     
                    '{:14.4e}'.format(s))
        if (r > 10000000 and x > 10000):
            print('{:8d}'.format(K),'\u2502',
                    '{:14.4e}'.format(x),'\u2502',
                    '{:13.4f}'.format(r),'\u2502',     
                    '{:14.4e}'.format(s))
        elif r <10000000:
            print ('{:8d}'.format(K),'\u2502',
                    '{:14.4f}'.format(x),'\u2502',
                    '{:13.4f}'.format(r),'\u2502',     
                    '{:14.4f}'.format(s))
        Nstep += step
    K += 1
    n += 2
if abs(r) > eps:
    print('Ряд не сошёлся')
else:
    print('Ряд сошелся за ',n,'итераций')
    print('Сумма:', s)
