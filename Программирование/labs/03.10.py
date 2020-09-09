 from math import exp
n=float(input('Введите начальное значение '))
k=float(input('Введите конечное значение '))
sh=float(input('Введите шаг '))
print('      \u004e    \u2502      \u0071      \u2502'
      +'      '+'\u0078\u2081      \u2502      \u0078\u2082')
print(33*'\u2501')
N=1
q=n
while q<=k:
    x1=2.97*(q**4)+4.84*(q**3)-16.4*q*q+41.2*q-33.2
    x2=2-(q*(exp(q)))
    print ('   ','{:3.0f}'.format(N).rjust(2),'   \u2502',
          '{:.4f}'.format(q).rjust(4),'     \u2502',
          '{:.4f}'.format(x1).rjust(8),'    \u2502',
          '{:.4f}'.format(x2).rjust(6))
    q=q+sh
    N=N+1
print(40*'\u2501')
print(20*' '+'Построение графика'+15*' ')
print(40*'\u2501')
print(' ')
print(60*'\u2501'+'\u003e'+' y')
print('X'+46*' '+'\u2502')
q=n
x1max=2.97*(k**4)+4.84*(k**3)-16.4*k*k+41.2*k-33.2
x1min=2.97*(n**4)+4.84*(n**3)-16.4*n*n+41.2*n-33.2
for i in range (0,N):
    x1=2.97*(q**4)+4.84*(q**3)-16.4*q*q+41.2*q-33.2
    """
    m1=(x1-x1max)/(x1max-x1min)
    m=int(m1)
    """
    x=int(x1)
    if x>0:
        print('{:.4f}'.format(x1).rjust(8)
              ,38*' '+'\u2502'+x*' '+'*')
    elif x<0:
        x=abs(x)
        print('{:.4f}'.format(x1).rjust(8)
              ,(37-x)*' '+'*'+x*' '+'\u2502')
    elif x==0:
        print('{:.4f}'.format(x1).rjust(8)
              ,38*' '+'*')
        
    q=q+sh
print(47*' '+'\u22c1')
print(47*' '+'x')
    
