# my base 2 function this gives the base plus 1 currently
def b2_fun(t):
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
b2_fun(4)
