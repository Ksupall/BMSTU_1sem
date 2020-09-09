print('Введите текст: ')
text = []
while True:
    x = input()
    text.append(x)
    if x[len(x)-1] == '.' or x[len(x)-1] == '!' or x[len(x)-1] == '?':
        break
text0 = []

for i in range(len(text)):
    k = text[i].strip()
    text0.append(k)
m = 0
for i in range(len(text0)):
    if len(text0[i]) > m:
        m = len(text0[i])
    razniza = m - len(text0[i])
"""
o = ''
for i in range(len(text0)):
    k = text0[i].split()
    razniza = m - len(text0[i])
    for j in range(len(text0[i])):
        if text0[i][j] != ' ' and j <= len(k[0]):
            o += text0[i][j]
        print(o)
    
            
    k = text0[i].split()
    razniza = m - len(text0[i])
    for j in range(len(k)):
    

for i in range(len(text0)):
    
print(razniza)
"""    
    
        

        
