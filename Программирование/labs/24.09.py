from math import sqrt,acos,cos,degrees,pi



x1,y1=map(float,input("Введите координаты первой точки ").split())
x2,y2=map(float,input("Введите координаты второй точки ").split())
x3,y3=map(float,input("Введите координаты третьей точки ").split())
a=sqrt((x2-x3)**2+(y2-y3)**2)
b=sqrt((x3-x1)**2+(y3-y1)**2)
c=sqrt((x2-x1)**2+(y2-y1)**2)
print("Длина отрезка а ",'{:.4f}'.format(a))
print("Длина отрезка b ",'{:.4f}'.format(b))
print("Длина отрезка с ",'{:.4f}'.format(c))
if (a+b>c and a+c>b and b+c>a):
    print ("Такой треугольник существует")
else:
    print ("Такой треугольник не существует")
if a==b==c:
    print ("Треугольник равносторонний")
else:
    print ("Треугольник неравносторонний")
if (a>=b and a>=c):
    v=((b*b+c*c-a*a)/2*b*c)/(pi*2)
    ugol=acos(v-int(v))
    bis=2*b*c*cos(ugol/2)/(b+c)
if (b>=c and b>=a):
    v=((a*a+c*c-b*b)/2*a*c)/(pi*2)
    ugol=acos(v-int(v))
    bis=2*a*c*cos(ugol/2)/(a+c)
if (c>=a and c>=b):
    v=((b*b+a*a-c*c)/2*b*a)/(pi*2)
    ugol=acos(v-int(v)) 
    bis=2*a*b*cos(ugol/2)/(a+b)
print (bis)
x0,y0=map(float,input("Введите координаты точки ").split())
w=0
if ((x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)>0 and (x2-x0)*(y3-y2)-(x3-x2)*(y2-y0)>0 and (x3-x0)*(y1-y3)-(x1-x3)*(y3-y0)>0):
    q=sqrt((x0-x1)**2+(y0-y1)**2)
    e=sqrt((x0-x2)**2+(y0-y2)**2)
    r=sqrt((x0-x3)**2+(y0-y3)**2)
    w=1
    print("Точка внутри треугольника")
if ((x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)<0 and (x2-x0)*(y3-y2)-(x3-x2)*(y2-y0)<0 and (x3-x0)*(y1-y3)-(x1-x3)*(y3-y0)<0):
    q=sqrt((x0-x1)**2+(y0-y1)**2)
    e=sqrt((x0-x2)**2+(y0-y2)**2)
    r=sqrt((x0-x3)**2+(y0-y3)**2)
    w=1
    print("Точка внутри треугольника")
if ((x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)==0 or (x2-x0)*(y3-y2)-(x3-x2)*(y2-y0)==0 or (x3-x0)*(y1-y3)-(x1-x3)*(y3-y0)==0):
    w=1
        
    print("Точка на стороне треугольника")
if w==0:
    print ("Точка вне треугольника")
