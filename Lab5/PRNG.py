import time
import numpy
primes = [3851, 4007, 4639, 5501, 6121]

def pseudo_rando_initial_values():
    cur_time = str(time.time())
    cur_time_no_dot = [int(l) for l in cur_time if l != '.']

    p = primes[sum(cur_time_no_dot)%5]
    q = primes[numpy.product(cur_time_no_dot)%5]
    return blum_blum_shub(p,q)


def blum_blum_shub(p, q):
    n = p * q
    s = ((n * p)/q)%n
    x = (s*s)%n
    y = x
    to_return = []
    for i in range(256):
        y = (x*x)%n
        x = y
        to_add = str(y%2)
        to_return.append(to_add)

    return to_return

key = pseudo_rando_initial_values()
time.sleep(4)
key2 = pseudo_rando_initial_values()
time.sleep(1)
key3 = pseudo_rando_initial_values()
print(''.join(key))
print
print ''.join(key2)
print
print ''.join(key3)