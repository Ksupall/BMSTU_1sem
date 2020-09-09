print('Введите элементы массива через пробел')
l = list(input('').split(' '))
kol = 0
k = 2
s = 1
q = 0
for i in range (len(l)):
    if str(l[i]).isdigit() == True:
        if l[i] == 1:
            kol += 1
        else:
            while int(l[i]) > s:
              n = k - 1 + k
              s += n
              k += 1
            if int(l[i]) == s:
                kol += 1
                k = 2
                s = 1
    elif str(l[i]).isdigit() == False:
        print('Неверный формат массива')
        q = 1
        break
if q == 0:
    print('Количество полных квадратов: ',kol)
