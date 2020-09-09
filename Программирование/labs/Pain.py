from tkinter import *
from math import sqrt
from tkinter.colorchooser import *
canvas_width = 700
canvas_height = 500
color = "black"
getx1 = -1
gety1 = -1
getx2 = -2
gety2 = -2
x1 = -1
y1 = -1
# РИСОВАНИЕ КАРАНДАШОМ    
def paint(event):
    brush_size = scale.get()
    global x1
    global y1
    if x1 == -1:
        x1=event.x 
        y1=event.y  
        x2 = x1
        y2 = y1
        w.create_oval(x1-brush_size, y1-brush_size ,x1+brush_size, y1+brush_size,
                      fill = color)
    else:
        x2=event.x 
        y2=event.y 
    w.create_line(x1, y1, x2, y2,
                fill = color, width = brush_size)
    w.create_oval(x2-brush_size, y2-brush_size ,x2+brush_size, y2+brush_size,
                     fill = color, outline = color)
    x1 = x2
    y1 = y2
def pensil():
    w.bind("<B1-Motion>", paint)
    w.bind("<B1-ButtonRelease>", xoff)
 # ЛАСТИК
def paint_bg(event):
    brush_size = scale.get()
    global x1
    global y1
    if x1 == -1:
        x1=event.x 
        y1=event.y  
        x2 = x1
        y2 = y1
        w.create_oval(x1-brush_size, y1-brush_size ,x1+brush_size, y1+brush_size,
                      fill = "white")
    else:
        x2=event.x 
        y2=event.y 
    w.create_line(x1, y1, x2, y2,
                fill = "white", width = brush_size)
    w.create_oval(x2-brush_size, y2-brush_size ,x2+brush_size, y2+brush_size,
                     fill = "white", outline = "white")
    x1 = x2
    y1 = y2
def rubbish():
    w.bind("<B1-Motion>", paint_bg)
    w.bind("<B1-ButtonRelease>", xoff)
def xoff(event):
    global x1
    global y1
    x1 = -1
    y1 = -1
# ПРЯМАЯ
def getXY1(event):
    global getx1
    global gety1
    getx1=event.x
    gety1=event.y
def new_line(event):
    global getx2
    global gety2
    global tl
    global getx1
    global gety1
    
    getx2=event.x
    gety2=event.y
    brush_size = scale.get()
    if tl == 0:
        tl = w.create_line(getx1, gety1, getx2, gety2, width = brush_size, fill = color)
    w.coords(tl, getx1, gety1, getx2, gety2)
    w.itemconfig(tl, fill = color, width = brush_size)
def getXY2(event):
    global getx2
    global gety2
    global getx1
    global gety1
    getx2=event.x
    gety2=event.y
    brush_size = scale.get()
    w.create_line(getx1, gety1, getx2, gety2, width = brush_size, fill = color)
    getx2=-1
    gety2=-1
    getx1=-1
    gety1=-1
def line():
    w.bind('<1>', getXY1)
    w.bind('<B1-ButtonRelease>',getXY2)
    w.bind('<B1-Motion>', new_line)
# ПРЯМОУГОЛЬНИК
def getsXY1(event):
    global getx1
    global gety1
    getx1=event.x
    gety1=event.y
def square():
    w.bind('<1>', getsXY1)
    w.bind('<B1-ButtonRelease>',getsXY2)
    w.bind('<B1-Motion>', new_square)
def getsXY2(event):
    global getx2
    global gety2
    global getx1
    global gety1
    getx2=event.x
    gety2=event.y
    brush_size = scale.get()
    w.create_line(getx1, gety1, getx1, gety2, width = brush_size, fill = color)
    w.create_line(getx1, gety2, getx2, gety2, width = brush_size, fill = color)
    w.create_line(getx2, gety2, getx2, gety1, width = brush_size, fill = color)
    w.create_line(getx2, gety1, getx1, gety1, width = brush_size, fill = color)
    getx2=-1
    gety2=-1
    getx1=-1
    gety1=-1
def new_square(event):
    global getx2
    global gety2
    global ts1
    global ts2
    global ts3
    global ts4
    global getx1
    global gety1    
    getx2=event.x
    gety2=event.y
    brush_size = scale.get()
    if (ts1 == 0 or ts2 == 0 or ts3 == 0 or ts4 == 0):
        ts1 = w.create_line(getx1, gety1, getx1, gety2, width = brush_size, fill = color)
        ts2 = w.create_line(getx1, gety2, getx2, gety2, width = brush_size, fill = color)
        ts3 = w.create_line(getx2, gety2, getx2, gety1, width = brush_size, fill = color)
        ts4 = w.create_line(getx2, gety1, getx1, gety1, width = brush_size, fill = color)
    w.coords(ts1, getx1, gety1, getx1, gety2)
    w.coords(ts2, getx1, gety2, getx2, gety2)
    w.coords(ts3, getx2, gety2, getx2, gety1)
    w.coords(ts4, getx2, gety1, getx1, gety1)    
    w.itemconfig(ts1, fill = color, width = brush_size)
    w.itemconfig(ts2, fill = color, width = brush_size)
    w.itemconfig(ts3, fill = color, width = brush_size)
    w.itemconfig(ts4, fill = color, width = brush_size)
# ОКРУЖНОСТЬ
def getcXY1(event):
    global getx1
    global gety1
    getx1=event.x
    gety1=event.y
def circle():
    w.bind('<1>', getcXY1)
    w.bind('<B1-ButtonRelease>',getcXY2)
    w.bind('<B1-Motion>', new_circle)
def getcXY2(event):
    global getx2
    global gety2
    global getx1
    global gety1
    getx2=event.x
    gety2=event.y
    brush_size = scale.get()
    r = sqrt((getx1 - getx2)**2 + (gety1 - gety2)**2)
    w.create_oval(getx1-r, gety1+r, getx1+r, gety1-r, outline = color, width = brush_size)
    getx2=-1
    gety2=-1
    getx1=-1
    gety1=-1
def new_circle(event):
    global getx2
    global gety2
    global tc
    global getx1
    global gety1    
    getx2=event.x
    gety2=event.y
    brush_size = scale.get()
    r = sqrt((getx1 - getx2)**2 + (gety1 - gety2)**2)
    if tc == 0:
        w.create_oval(getx1-r, gety1+r, getx1+r, gety1-r, outline = color, width = brush_size) 
    w.coords(tc,getx2, gety2)
    w.itemconfig(tc, fill = color, width = brush_size)
def color_change(new_color):
    global color
    color = new_color
def getColor():
    global color
    color = (askcolor())[1]
    butc.config(bg = color)
root = Tk()
root.title('Paint на Питоне')
but1 = Button(root,text = "Прямая", width = 10, command = line)
but1.grid(column = 8, row = 0)
but2 = Button(root,text = "Карандаш",width = 10, command = pensil)
but2.grid(column = 9, row = 0)
but3 = Button(root,text = "Ластик",width = 10, command = rubbish)
but3.grid(column = 8, row = 1)
but4 = Button(root,text = "Текст",width = 10)
but4.grid(column = 9, row = 1)
but5 = Button(root,text = "Окружность",width = 10, command = circle)
but5.grid(column = 8, row = 2)
but6 = Button(root,text = "Прямоугольн",width = 10, command = square)
but6.grid(column = 9, row = 2)
butc = Button(root,text = "Цвет", width = 10, bg = "black", fg = "white",
                command= getColor)
butc.grid(column = 8, row = 8)
w = Canvas(root,
           width=canvas_width,
           height=canvas_height,
           bg = "white")
tl = 0
ts1 = 0
ts2 = 0
ts2 = 0
ts3 = 0
tc = 0
'''
size = Label(text = "Изменение размера кисти")
size.grid(column = 8, row = 2)
'''
scale = Scale(root,
              length = 200, from_=1, to=15,
              resolution = 1)
scale.grid(column = 9
           , row = 8, padx=15)
w.grid(row = 0, column = 0,
       columnspan = 7,rowspan = 15, padx = 50, pady = 5,
       sticky = E+W+S+N)
w.columnconfigure(6, weight = 1)
w.rowconfigure(2, weight = 1)
root.mainloop()
































