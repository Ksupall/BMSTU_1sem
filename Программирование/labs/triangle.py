"""
from tkinter import *
root=Tk()
var=IntVar()
rbutton1=Radiobutton(root,text='1',variable=var,value=1)
rbutton2=Radiobutton(root,text='2',variable=var,value=2)
rbutton3=Radiobutton(root,text='3',variable=var,value=3)
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()
root.mainloop()

H1=30
W1=80
def output(event):
     s = ent.get()
     if s == "1":
          tex.delete(1.0,END)
          tex.insert(END,"1")
     elif s == "2":
          tex.delete(1.0,END)
          tex.insert(END,"2")
     else:
          tex.delete(1.0,END)
          tex.insert(END,"Введите 1 или 2 в поле слева")
 
from tkinter import *
root = Tk()
ks = Entry(root,width=40)
ent = Entry(root,width=2)
but = Button(root,text="Вывести")
tex = Text(root,width=W1,height=H1,font="8",wrap=WORD)
text1 = Text(root,height=7,width=7,font='Arial 14',wrap=WORD)

ent.grid(row=0,column=0,padx=150)
but.grid(row=0,column=1)
tex.grid(row=0,column=20,padx=50,pady=10)
ks.grid(row=0,column=13)
text1.grid(row=0,column=12)


but.bind("<Button-1>",output)
 
root.mainloop() 
"""
from tkinter import *
root=Tk()
text1=Text(root,height=7,width=7,font='Arial 14',wrap=WORD)
text1.pack()
root.mainloop()
