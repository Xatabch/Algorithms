from polynom import *
import copy

def get_legendge_polynomial(n):
    if not n:
        return Polynomial(0, [1])
    if n == 1:
        return Polynomial(1, [1, 0])

    zero = Polynomial(0, [1])
    one = Polynomial(1, [1, 0])
    m = 1
    for i in range(n - 1):
        buf_one = copy.deepcopy(one)
        buf_zero = copy.deepcopy(zero)

        buf_one.up_degree()
        buf_one *= ((2 * m + 1)/(m + 1))
        buf_zero *= (m / (m + 1))
        buf_one -= buf_zero

        zero = one
        one = buf_one

        m += 1

    print(one)


    return one
