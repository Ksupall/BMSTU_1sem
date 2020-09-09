print('Введите текст: ')
text = []
while True:
    x = input()
    text.append(x)
    if x[len(x)-1] == '.' or x[len(x)-1] == '!' or x[len(x)-1] == '?':
        break
k = []
n = 0
for i in range(len(text)):
    k += text[i].split()
for i in range(len(k)):
     k[i].endswith('.')== True:
        n += 1
print(n)

"""
    while (k[i].endswith('.')== False or k[i].endswith('!')== False or
        k[i].endswith('?')== False):
        print('yes')
print(n)    
"""
