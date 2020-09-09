def creatArray():
    r = 0
    x = int(input('Введите число n: '))
    y = int(input(''))
    array = []

    for i in range (x):
        array.append([])
        for i in range (y):
            array[i].append(r)
            r += 1
    print('Матрица: ')
    for u in range (x):
        print(array[u])

    colomn = 0
    colomnIter = 1
    m = 0

    for l in range (y):
        s = 0
        for o in range (x):
            s += array[o][l]
        print("%3d" % (s), end = '')
        if (m < s):
            m = s
            colomn += colomnIter
        else:
            colomnIter += 1

    print("\nМаксимальный столб имеет сумму: %3d\nИ этот столбец под номером %2i" % (m,colomn))
creatArray()
