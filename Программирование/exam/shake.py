a = list(map(float,input('Введите массив чисел: ').split()))
def shakerSort(a): 
    #lb, ub границы неотсортированной части массива
    k = r = len(a)-1
    l = 1
    while ( l < r ):
        # проход сверху вниз 
        for i in range (r, l-1, -1):
            if a[i-1] > a[i]: 
                a[i-1], a[i] = a[i], a[i-1]
                k = i
            l = k
        # проход снизу вверх 
        for i in range (l, r+1):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                k = i
            r = k
    return a
print(shakerSort(a))
