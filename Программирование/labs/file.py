inputfile = "text.txt"
f = open('text.txt', mode = 'r')
for num, line in enumerate(f,1):
    if 'Ирина' in line:
        print(str(num)+')'+'Hello, '+line.strip())
