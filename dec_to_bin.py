# my base 2 function this gives the base plus 1 currently
def b2_fun(t):
    f = int()
    f = 0
    if t != 1 and t % 2 != 0:
        f = t - (t % 2)
    else:
        f = t
    n = 0
    while f != 0:
        f = f // 2
        n = n + 1
    return n
# finding the remainder
lam_fig = lambda b, n : b - 2**(n-1)
#printing the decimal to binary
byte_inp = ("00000000")
for b in range(1,256,1):
    byte_list = list(byte_inp)
    byte_list[(b2_fun(b)-1)] = "1"
    r = lam_fig(b,b2_fun(b))
    while r != 0:
        byte_list[(b2_fun(r)-1)] = "1"
        r = lam_fig(r,b2_fun(r))
    print(f'{"".join(byte_list[::-1])} decimal is {b}')
