# my base 2 tool!
for t in range(1,65,1):
    f = int()
    if t != 1 and t % 2 != 0:
        f = t - (t % 2)
    else:
        f = t
    n = 0
    while f != 0:
        f = f // 2
        n = n + 1
    print(f'{n} input: {t}')
