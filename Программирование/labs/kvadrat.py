from tkinter import *
root = Tk()
root.title('Квадрат')
root.geometry('1020x620')
c = Canvas(root, width=1020, height=620, bg='white')
image = c.create_rectangle(100, 100, 50, 50, fill='pink')
"""
c.move(image, 0, 150)
c.itemconfig(image,outline="red",width=3)
c.coords(image,300,200,450,450)
def mooove(event):
     c.move(image,2,2)
c.bind('<Button-1>',mooove)
"""
x = 2
y = 0
def move():
    c.move(image, x, y)
def main():
    move()
    root.after(50, main)
main()
"""
while x2 != 300:
    image = c.create_rectangle(x1, y1, x2, y2, fill='pink')
    x1 += 2
    y1 += 0
    x2 += 2
    y2 += 0
"""
c.pack()
root.mainloop()
