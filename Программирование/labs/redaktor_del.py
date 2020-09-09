"""
pz - точка, запятая или другой разделитель
orig - слова с точкой до того, как убираем точку
"""
a = str(input('Введите строку: '))
b = str(input('ВВедите слово, которое надо убрать: '))
al = a.split(' ')
for i in range(len(al)):
    if al[i].isalnum():
        if al[i] == b:
            al[i] = ''
    else:
        d = len(al[i])
        c = []
        for j in range(len(al[i])):
            c.append(al[i][j])
        pz = c[d-1]
        orig = ''.join(c) 
        c.remove(c[d-1])
        sl = ''.join(c)
        al[i] = sl
        if al[i] == b:
            al[i] = pz
        else:
            al[i] = orig
vse = ' '.join(al)
print(vse)
