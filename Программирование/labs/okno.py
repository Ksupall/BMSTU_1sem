from tkinter import *
from math import sin, cos
root = Tk()
root.title('Первое окно в Питоне')
root.geometry('1020x620')
canvas = Canvas(root, width=1020, height=620, bg='#002')
for i in range(21):
    k = 50*i
    canvas.create_line(10+k, 610, 10+k, 10, width=1, fill ='#007')
for i in range(13):
    k =50*i
    canvas.create_line(10, 10+k, 1010, 10+k, width=1, fill='#007')
canvas.create_line(10, 10, 10, 610, width=1, arrow=FIRST, fill='white')
canvas.create_line(1010, 310, 10, 310,  width=1, arrow=FIRST, fill='white')
w = 0.02
phi = 10
A = 100
dy = 310
xy = []
for x in range(1000):
    y = sin(x*w)
    xy.append(x + phi)
    xy.append(y*A + dy)
sin_line = canvas.create_line(xy, fill='pink')
yx = []
for x in range(1000):
    y = cos(x*w)
    yx.append(x + phi)
    yx.append(y*A + dy)
cos_line = canvas.create_line(yx, fill='blue')
canvas.pack()
root.mainloop() 
