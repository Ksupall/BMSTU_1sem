"""
Полякова Ксения ИУ7-12Б

a-коэффициент a
b-коэффициент b
c-коэффициент c
D-дискриминант
""""
from math import sqrt
a=float(input())
b=float(input())
c=float(input())

if a!=0:
    D=b*b-4*a*c
    if D>0:
        print((-b-sqrt(D))/2*a)
        print((-b+sqrt(D))/2*a)
    if D<0:
        print("нет действительных решений")
    if D==0:
        print(-b/2*a)
else:
    if b==0:
        if c==0:
            print ("x-любое число")
        else:
            print("нет решений")
    else:
        print(-c/b)
        
    
