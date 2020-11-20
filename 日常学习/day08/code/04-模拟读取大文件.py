def func():
    f = open(file='bb.txt', mode='r', encoding='utf-8')

    while True:
        buf = f.read(40960)
        if buf:
            print(buf, enc='')
        else:
            break

    f.close()

def func2():
    f = open(file='bb.txt', mode='r', encoding='utf-8')
    for line in f:
        print(line,end='')
    f.close()
