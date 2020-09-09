a = int(input('Введите количество строк: '))
b = int(input('Введите количество столбцов матрицы: '))
m = []
for i in range(a):
    x = list(map(float,input().split()))
    m.append(x)
def sol(m):
    s1 = 0
    s2 = 0
    for i in range(1,b):
        for j in range(a):
            s1 += m[j][i-1]
            s2 += m[j][i]
        sa1 = s1 / a
        sa2 = s2 / a
        s1 = 0
        s2 = 0
        if sa1 > sa2:
            for u in range(a):
                m[u][i], m[u][i-1] = m[u][i-1], m[u][i]
    return m
m = sol(m)
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end = ' ')
    print()
kolu = 0
kold = 0
for i in range(len(sol(m))):
    for j in range(len(sol(m)[i])):
        if j >= i:
            if m[i][j] % 5 == 0:
                kolu += 1
        if j <= i:
            if m[i][j] % 5== 0:
                kold += 1
if kolu > kold:
    print('Vverxniye')
if kold > kolu:
    print('Nigniye')
