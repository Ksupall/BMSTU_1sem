from tkinter import *
from random import *
canvas_width = 700
canvas_height = 500
brush_size = 2
color = "black"
def paint(event):
    global brush_size
    global color
    x1=event.x+brush_size
    x2=event.x-brush_size
    y1=event.y+brush_size
    y2=event.y-brush_size
    w.create_oval(x1, y1, x2, y2,
                      fill = color,
                      outline = color)
def brush_size_change(new_size):
    global brush_size
    brush_size = new_size
def color_change(new_color):
    global color
    color = new_color
def size_change(root):
    a = scale.get()
    brush_size_change(a)    
root = Tk()
root.title('Paint на Питоне')
w = Canvas(root,
           width=canvas_width,
           height=canvas_height,
           bg = "white")
w.bind("<B1-Motion>", paint)
size = Label(text = "Изменение размера кисти")
size.grid(column = 7, row = 0)
scale = Scale(root,orient = "horizontal",
              length = 200, from_=1, to=50,
              resolution = 1)
scale.grid(column = 7, row = 1, padx=15)
but_size = Button(root, text = "Изменить")
but_size.grid(column = 7, row = 2)
but_size.bind("<Button-1>", size_change)
w.grid(row = 1, column = 0,
       columnspan = 7, padx = 50, pady = 5,
       sticky = E+W+S+N)
w.columnconfigure(6, weight = 1)
w.rowconfigure(2, weight = 1)
root.mainloop()
"""

"""
'''
x1 = -1
y1 = -1

def paint(event):
    global brush_size
    global color
    global x1
    global y1
    if x1 == -1:
        x1=event.x
        y1=event.y
        x2 = x1
        y2 = y1
    else:
        x2=event.x 
        y2=event.y 
    w.create_line(x1, y1, x2, y2,
                      fill = color)
    x1 = x2
    y1 = y2
def xoff(event):
    global x1
    global y1
    x1 = -1
    y1 = -1
'''
