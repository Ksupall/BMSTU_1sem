# Уточнение корней методом простых итераций
#                           Громова ИУ7-21Б
# *_label *_labels - переменные для label
# *_entry - переменные для полей ввода
# *_button - переменные для кнопок
# x, x0, x1 - аргументы
# low, a, high, b - значение границ отрезков
# error - номер ошибки
# y - значение функции
# i - количество итераций, за которое нашелся корень
# err - словарь ошибок
# res_arr - массив корней
# j, k, a, b, n, e, h - рабочие переменные

from tkinter import *
import numpy as np
from math import cos, pi, sin
from tkinter import messagebox
import matplotlib.pyplot as plt


root = Tk()
root.title('Уточнение корней')
root.minsize(1024,480)


# Функция f(x)
def f(x):
    #return cos(x)
    return x - cos(x)

# Функция, возвращающая значение x
def X(x):
    #return x + cos(x)
    return cos(x)

def proizv_1_f(x):
    #return -sin(x)
    return 1 + sin(x)

# Производная от функции f(x)
def proizv_2_f(x):
    #return -cos(x)
    return cos(x)

# Производная от функции X(x)
def proizv_3_f(x):
    #return sin(x)
    return -sin(x)

# Функция, вычисляющая приближенное значение корня на элементарном интервале
def calc_root(low, high, N, eps):
    i = 1
    x0 = (low + high) / 2    
    x1 = X(x0)
    error = 0
      
    while abs(x0 - x1) > eps:        
        if x0 < low:
            error = 1
            return error, "low"
        if x0 > high:
            error = 2
            return error, "high"
        if i > N:
            error = 3
            return error, "iteration"

        x0 = x1
        x1 = X(x0)
        i += 1
        y = f(x1)
        #print("x0 = {:4.4f} current x1  = {:4.4f}, iteration = {:4d}".format(x0,x1,i))
            
    return x1, i

# Функция, вычисляющая точки перегиба
def calc_peregib(low, high, N, eps):
    i = 1
    x0 = low
    x1 = x0 - (proizv_2_f(x0)/proizv_3_f(x0))
    while abs(x0 - x1) > eps:
        if x0 >= low and x0 <= high:
            x0 = x1
            x1 = x0 - (proizv_2_f(x0)/proizv_3_f(x0))
            i += 1
        else:
            x1 = 'err'
            break
        
    return x1

def absolute_root(low, high, N, eps):
    i = 1
    x0 = low
    x1 = x0 - (f(x0)/proizv_1_f(x0))
    while abs(x0 - x1) > eps:
        if x0 >= low and x0 <= high:
            x0 = x1
            x1 = x0 - (f(x0)/proizv_1_f(x0))
            i += 1
        else:
            x1 = 'err'
            break
        
    return x1
    

# Функция, проверяющая введенные значения
def check_input(num):
    c = num.count('.')
    if (num.isdigit() == False and num.isalnum() == True) or (c > 1) or (num == ''):
        return True
    else:
        return False


# Функция, вычисляющая приближенный корень на введенном интервале    
def calc(a, b, h, n, e):
    err = {"low":1,
           "high":2,
           "iteration":3}
    global total_tabel_labels
    total_tabel_labels = []
    global j
    j = 0
    res_arr = []
    i = a
    lates_t = h
    while(i < b):
        if (i + h) > b:
            res, iter_num = calc_root(i, b, n, e)
            top = b
        else:
            res, iter_num = calc_root(i, i+h, n, e)
            top = i + h

        if iter_num not in err:
            r_labels = []
            for k in range(6):
                r_label = Label(root, width = 15, relief = 'solid')
                r_label.grid(row = 9+j, column = 0+k ,\
                             sticky = 'nsew', padx = 1, pady = 1)
                r_labels.append(r_label)

            r_labels[0]['text'] = str(j + 1)
            r_labels[1]['text'] = '[ '+'{:0.2f}'.format(i)+' ; '+'{:0.2f}'.format(top)+' ]'
            r_labels[2]['text'] = '{:4.6e}'.format(res)
            r_labels[3]['text'] = '{:.0e}'.format(f(res))
            r_labels[4]['text'] = '{:d}'.format(iter_num)
            r_labels[5]['text'] = '0'
            j += 1

            total_tabel_labels.append(r_labels)
            res_arr.append(res)

        else:
            # Проверка наличия корня на элементарном интервале (если корень не нашелся по методу)
            if f(i)*f(top) < 0 or (f(i)*f(top) == 0 and (i != latest_t)): 
                latest_t = top
                
                r_labels = []
                for k in range(6):
                    r_label = Label(root, width = 15, relief = 'solid')
                    r_label.grid(row = 9+j, column = 0+k ,\
                                 sticky = 'nsew', padx = 1, pady = 1)
                    r_labels.append(r_label)

                r_labels[0]['text'] = str(j + 1)
                r_labels[1]['text'] = '[ '+'{:0.2f}'.format(i)+' ; '+'{:0.2f}'.format(top)+' ]'
                r_labels[2]['text'] = '---'
                r_labels[3]['text'] = '---'
                r_labels[4]['text'] = '---'
                r_labels[5]['text'] = '{:d}'.format(err[iter_num])
                j += 1
                total_tabel_labels.append(r_labels)
        
        i += h
    if j == 0:
        global no_roots_label
        no_roots_label = Label(root, text = "Нет корней", font = 'arial 20')
        no_roots_label.grid(row = 9, column = 0, columnspan = 5)



# Функция очистки полей ввода
def clear_entry():
    a_entry.delete(0, END)
    b_entry.delete(0, END)
    h_entry.delete(0, END)
    n_entry.delete(0, END)
    e_entry.delete(0, END)

# Функция очистки label    
def clear_labels():
    
    for k in range(len(total_tabel_labels)):
        for d in range(len(total_tabel_labels[k])):
            total_tabel_labels[k][d].destroy()

    peregib_label['text'] = 'Точки перегиба = '
    if j == 0:
        no_roots_label.destroy()

# Функция очистки всего 
def clear():
    clear_entry()
    clear_labels()

# Функция, получающая значения из полей ввода    
def get_data():
    a_inp = a_entry.get()
    b_inp = b_entry.get()
    h_inp = h_entry.get()
    n_inp = n_entry.get()
    e_inp = e_entry.get()
    
    if check_input(a_inp) or check_input(b_inp) or check_input(h_inp)\
       or (check_input(n_inp)) or (n_inp.count('.') > 0) or (check_input(e_inp))\
       or (a_inp == '0' and b_inp == '0' and h_inp == '0' and n_inp == '0'\
       and e_inp == '0'):
        messagebox.showinfo('Ошибка', 'Некорректный ввод')
        clear_entry()
    else:
        if float(a_inp) < float(b_inp):
            a_inp = float(a_inp)
            b_inp = float(b_inp)
            h_inp = float(h_inp)
            n_inp = int(n_inp)
            e_inp = float(e_inp)
            calc(a_inp, b_inp, h_inp, n_inp, e_inp)
            
        else:
            messagebox.showinfo('Ошибка', 'Некорректный ввод (a >= b)')
            clear_entry()

# Функция, рисующая график            
def graph():
    plt.close()
    a = float(a_entry.get())
    b = float(b_entry.get())
    h = 0.001
    n = float(n_entry.get())
    e = float(e_entry.get())
    x1 = []
    y1 = []
    x2 = set()
    y2 = []
    y3 = []
    x4 = set()
    y4 = []
    i = a
    while (i < b):
        x1.append(i)
        y1.append(f(i))
        y3.append(0)
        i += 0.02

    i = a
    k = 0
    while (i <= b):
        res1 = calc_peregib(i, i + h, n, e)
        res2 = absolute_root(i, i + h, n, e)
        i += h
        if res1 != 'err':
            x2.add(round(res1,4))
        if res2 != 'err':
            x4.add(res2)
                       
    x2 = list(x2)
    x4 = list(x4)
    for k in range(len(x2)):
        y2.append(f(x2[k]))
    for k in range(len(x4)):
        y4.append(f(x4[k]))

    if x2:
        peregib_label['text'] = 'Точки перегиба: \n'
        for k in x2:
            peregib_label['text'] += '{:4.5e}\n'.format(k)

    else:
        peregib_label['text'] = 'В заданном интервале нет точек перегиба'

        
    plt.plot(x1, y1, label = 'График функции')
    plt.plot(x2, y2, 'ro', label = 'Точки перегиба')
    plt.plot(x1, y3)
    plt.plot(x4, y4, 'bo', label = 'Корни уравнения')
    plt.legend()
    plt.show()


    
# labels

welcome_label = Label(root, text = 'Уточнение корней методом простых итераци\
\nФункция f(x) = x - Cos(x)', font = 'arial 12')
welcome_label.grid(row = 0, column = 0, columnspan = 8)

inter_label = Label(root, text = 'Введите границы отрезка')
inter_label.grid(row = 1, column = 0, columnspan = 3, sticky = 'w')

inter1_label = Label(root, text = 'от:')
inter1_label.grid(row = 1, column = 2)

inter2_label = Label(root, text = 'до:')
inter2_label.grid(row = 1, column = 4)

step_label = Label(root, text = 'Введите шаг:')
step_label.grid(row = 2, column = 0, sticky = 'w')

n_label = Label(root, text = 'Введите количество итераций:')
n_label.grid(row = 3, column = 0, columnspan = 3, sticky = 'w')

e_label = Label(root, text = 'Введите точность:')
e_label.grid(row = 4, column = 0, sticky = 'w')

head_t_labels = []
for i in range(6):
    t_label = Label(root, width = 15, relief = 'solid')
    t_label.grid(row = 8, column = 0+i , sticky = 'nsew', padx = 1, pady = 1)
    head_t_labels.append(t_label)
head_t_labels[0]['text'] = 'N' 
head_t_labels[1]['text'] = 'эл. интервал'
head_t_labels[2]['text'] = 'значение x'
head_t_labels[3]['text'] = 'f(x)'
head_t_labels[4]['text'] = 'кол-во итераций'
head_t_labels[5]['text'] = 'код ошибки'

err_label = Label(root, text = 'Код ошибки:\n"0" - ошибок нет\n"1"\
- вычисления вышли за нижнюю границу элементарного интервала\
\n"2" - вычисления вышли за верхнюю границу элементарного интервала\n"3"\
- вычисления не достигли точности за количество итераций\n')
err_label.grid(row = 7, column = 0, columnspan = 5, sticky = 'w')

peregib_label = Label(root, text = 'Точки перегиба = ')
peregib_label.grid(row = 1, rowspan = 10, column = 10, columnspan = 4)

# enteries

a_entry = Entry(root, width = 7, bd = 5)
a_entry.grid(row = 1, column = 3)

b_entry = Entry(root, width = 7, bd = 5)
b_entry.grid(row = 1, column = 5)

h_entry = Entry(root, width = 7, bd = 5)
h_entry.grid(row = 2, column = 3)

n_entry = Entry(root, width = 7, bd = 5)
n_entry.grid(row = 3, column = 3)

e_entry = Entry(root, width = 7, bd = 5)
e_entry.grid(row = 4, column = 3)

# buttons

submit_button = Button(root, width = 20, text = 'Вычислить корни',\
                       command = get_data)
submit_button.grid(row = 5, column = 0, columnspan = 2)

clear_button = Button(root, text = 'Очистить', width = 20, command = clear)
clear_button.grid(row = 5, column = 3)

graph_button = Button(root, text = 'Построить график', width = 20, command = graph)
graph_button.grid(row = 6, column = 0, columnspan = 2)


root.mainloop()
