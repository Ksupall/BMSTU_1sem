n = str(input('Введите n: '))
test1 = n.isdigit()
if test1 == True:
    print('Введите матрицу по', n,'элементов в ряд через пробел')
    k = -1000000
    a = []
    I = 0
    J = 0
    a = [[j for j in input().split()] for i in range (int(n))]
    if a == 1:
        for i in range (int(n)):
            for j in range (int(n)):
                 if int(a[i][j]) > k and i%2 == 0 and j%2 == 0:
                    k = int(a[i][j])
                    I = i
                    J = j
        print('Элемент',k,'с индексами i =',I,'j = ',J,'наибольший')
    else:
        print('Неверный формат ввода')
else:
    print('Неверный ввод числ n')
