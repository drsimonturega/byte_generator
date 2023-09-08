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
    return n
# finding the remainder
lam_fig = lambda b, n : b - 2**(n-1)
# converting decimal to binary
def decto_byt(b):
    byte_inp = ("00000000")
    byte_list = list(byte_inp)
    byte_list[(b2_fun(b)-1)] = "1"
    r = lam_fig(b,b2_fun(b))
    while r != 0:
        byte_list[(b2_fun(r)-1)] = "1"
        r = lam_fig(r,b2_fun(r))
    byte_out = "".join(byte_list[::-1])
    return byte_out


ls_byt = [decto_byt(x) for x in range(1,256,1)]
for i in ls_byt:
    print(i)

