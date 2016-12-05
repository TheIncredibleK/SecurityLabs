import scipy.special as spc
import math

p = 6121
q = 3851

def blum_blum_shub(p, q):
    n = p * q
    s = ((n * p)/q)%n
    x = (s*s)%n
    to_return = []
    for i in range(200):
        y = (x*x)%n
        x = y
        to_add = str(y%2)
        to_return.append(to_add)

    return to_return

key = blum_blum_shub(p,q)


## monobit test from r4and0m
def monobit(bin_data):
    count = 0

    for bit_number in bin_data:
        if bit_number == '0':
            count -= 1
        else:
            count += 1

    sobs = count / math.sqrt(len(bin_data))
    p_val = spc.erfc(math.fabs(sobs) / math.sqrt(2))
    return p_val
data__ = ''.join(key)
print data__
print monobit(data__)


