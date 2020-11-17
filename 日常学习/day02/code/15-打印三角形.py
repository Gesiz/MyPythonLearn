n = 5
i = 1
while i <= n:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1

i = 1
while i <= n:
    j = 0
    while j < (n + 1 - i):
        print('*', end=' ')
        j += 1
    print()
    i += 1

