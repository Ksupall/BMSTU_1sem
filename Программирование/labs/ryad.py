shag = int(input('Shag: '))
eps = float(input('Eps: '))
x = float(input('x: '))
N = int(input('N: '))

s = 1
k0 = -x/2
ch = 3
zn = 2
k1 = k0*((-1/2)*(ch/zn)*x)
n = 1

print('\u250c'+7*'\u2500'+'\u252c'+12*'\u2500'+'\u2510')
print('\u2502   N   \u2502    Y        \u2502')
print('\u251c'+7*'\u2500'+'\u253c'+12*'\u2500'+'\u2524')
print('\u2502 ', '{:4.0f}'.format(float(n)),'\u2502', '{:5.3e}'.format(k0).rjust(5),'\u2502')

if abs(k0-k1)<eps:
        print('\u2514'+7*'\u2500'+'\u2534'+10*'\u2500'+'\u2518')
        print('За ',n, 'итераций сошлось.')
        
else:
        while abs(k1-k0)>eps:
                if n>=N:
                        print('\u2514'+7*'\u2500'+'\u2534'+12*'\u2500'+'\u2518')
                        print('За',N, 'итераций не сошлось.')
                        break
                else:
                        for i in range(shag):
                                if n>=N:
                                        break
                                ch += 2
                                zn += 1
                                k0, k1 = k1, k1*(-1/2)*(ch/zn)*x
                                s+=k1
                                n+=1
                        if n<N:
                                print('\u2502 ', '{:4.0f}'.format(float(n)),'\u2502', '{:5.3e}'.format(k0).rjust(10),'\u2502')

        if n<N:
                print('S =','{:5.3f}'.format(s),'\nКоличество итераций =', n)


