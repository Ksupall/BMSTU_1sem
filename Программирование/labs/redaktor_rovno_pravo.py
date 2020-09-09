print('Введите текст: ')
text = []
kol = 0
while True:
    x = input()
    kol += 1
    text.append(x)
    if x[len(x)-1] == '.' or x[len(x)-1] == '!' or x[len(x)-1] == '?':
        break
m = 0
mnum = 0
for i in range(len(text)):
    if len(text[i]) > m:
        m = len(text[i])
        mnum = i
for i in range(kol):
    k = len(text[i])
    print(' '*(m - k)+text[i])

        
