from math import *

a_min = float (input('Введите min: '))
a_step = float (input('Введите step: '))
a_max = float (input('Введите max: '))

a_min1 = int(a_min*100)
a_max1 = int(a_max*100)
a_step1 = int(a_step*100)
             
t = 1
M = int((a_max - a_min)/a_step)
c_min = 0.1234567890 
c_max = 0.1234567890
z = 0

for i in range (a_min1, a_max1+a_step1, a_step1):
    if i <= a_max1:
        i = i / 100
        c2 = sin(i) 
        if c_min == 0.1234567890 or c_min > c2:
            c_min = float('{:13.2f}'.format(c2))
        if c_max == 0.1234567890 or c_max < c2:
            c_max = float('{:13.2f}'.format(c2))
        t+=1

print ('\n\n\n')

c_delta = float('{:13.2f}'.format((c_max - c_min)/4))
c_gr_step = (c_max - c_min)/57
c1_min = abs(c_min)

while c1_min > 0:
    z += 1
    c1_min -= c_gr_step
osX = z

c2_min = c_min 
print('\n       ', end = '')
for k in range (1,6):
    r = int(57/5)-2
    if c2_min < 0 :
        print(c2_min, ' '*r, end = '')
    else:
        print(c2_min, ' '*r, end = '')
    c2_min=round((c2_min+c_delta),2)
    
print('\n         ','\u253c\u252c\u252c\u252c'*14,'\u253C', '\U00002500\U00002500→',' y',sep = '')

if c_min <= 0:
    print('         '+(' '*(z)),'|',sep = '')
    for i in range (a_min1, a_max1+a_step1, a_step1):
        if i <= a_max1:
            i = i / 100
            print('{:9.3f}'.format(i), end = '')
            c2 = sin(i)
            z = osX 
            if c2 > 0:
                while c2 > 0:
                    z +=1
                    c2 -= c_gr_step
            if c2 < 0:
                while c2 < 0:
                    z -=1
                    c2 += c_gr_step
            if  z > osX:
                print(' '*(osX) +'|', end = '')
                print(' '*(z-osX) +'*')
            if  z < osX:
                print(' '*(z) +'*', end = '')
                print(' '*(osX-z-1) +'|')
            if  z == osX:
                print(' '*(z) +'*')
            
if c_min > 0:
    for i in range (a_min1, a_max1+a_step1, a_step1):
        if i <= a_max1:
            i = i / 100
            print('{:9.3f}'.format(i), end = '')
            c2 = sin(i)
            c2 = round(c2, 2)
            z = 0
            if c2 > c_min:
                while c2 >= c_min:
                    z +=1
                    c2 -= c_gr_step
            print(' '*(z)+'*')
