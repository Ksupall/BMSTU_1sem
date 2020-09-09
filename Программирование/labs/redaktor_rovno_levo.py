print('Введите текст: ')
text = []
while True:
    x = input()
    text.append(x)
    if x[len(x)-1] == '.' or x[len(x)-1] == '!' or x[len(x)-1] == '?':
        break
for i in range(len(text)):
    k = text[i].lstrip()
    print(k)
