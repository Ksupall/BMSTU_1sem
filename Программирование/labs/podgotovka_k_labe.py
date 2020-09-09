from tkinter import *
root=Tk()
a = list(map(int,input('Введите координаты 3 вершин треугольника: ').split()))
x1 = a[0]
y1 = a[1]
x2 = a[2]
y2 = a[3]
r = int(input('Введите радиус окружности: '))
b = list(map(int,input('Введите координаты центра окружности: ').split()))
k = (y2 - y1)/(x2 - x1)
m = y1 - k*x1
print(k,m)
A = 1 + k*k
B = (-2)*b[0] + 2*k*(m - b[1])
C = b[0]**2 + (m - b[1])**2 - r*r
D = B*B - 4*A*C
if D > 0:
    from math import sqrt
    X1 = ((-1)*B - sqrt(D))/2*A
    X2 = ((-1)*B + sqrt(D))/2*A
    print(X1,X2)
if D == 0:
    X = (-1)*B/2*A
    print(X)
if D < 0:
    print('Корней нет!')
root.title('Треугольник и круг')
root.geometry('1020x620')
canvas = Canvas(root, width=1020, height=620, bg='white')
canvas.create_oval(b[0]-r,b[1]-r,b[0]+r,b[1]+r,fill = "white")
canvas.create_line(a[0], a[1], a[2], a[3], a[4], a[5], a[0], a[1])
canvas.pack()
root.mainloop()
