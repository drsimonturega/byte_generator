# my base 2 tool!
for t in range(1,17,1):
    f = int()
    if t != 1 and t % 2 != 0:
        f = t - (t % 2)
    else:
        f = t
    #print(f'this is f in for loop {f}')
    n = 0
    while f != 0:
        f = f // 2
        #print(f'this is f in while loop {f}')
        #print(f'this is n in while loop {n}')
        n = n + 1
    print(f'base 2 floor power: {n} input: {t}')
