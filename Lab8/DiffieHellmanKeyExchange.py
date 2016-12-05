from random import randint
from math import pow

def get_roots():
    def gcd(a,b):
        while b != 0:
            a, b = b, a % b
        return a

    def get_primitive_roots(modulo):
        roots = []
        required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

        for g in range(1, modulo):
            actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
            if required_set == actual_set:
                roots.append(g)
        return roots
    prime_roots = []
    prime_modulus = 0
    while(len(prime_roots) < 1):
        prime_modulus = randint(1,10)
        prime_roots = get_primitive_roots(prime_modulus)


    prime_roots = get_primitive_roots(prime_modulus)
    initial_base = prime_roots[randint(0, len(prime_roots)-1)]
    alice_number = randint(1, prime_modulus-1)
    bob_number = randint(1, prime_modulus-1)

    A = (pow(initial_base,alice_number)) % prime_modulus
    B = (pow(initial_base, bob_number)) % prime_modulus

    s1 = (B**alice_number)%prime_modulus
    s2 = (A**bob_number)%prime_modulus
    return s1, s2, prime_modulus, initial_base, alice_number, bob_number

s1, s2, prime_modulus, inital_base, alice_number, bob_number = get_roots()

print "Initial Agreed Base: " + str(inital_base)
print "Prime Modulus :" + str(prime_modulus)
print "Alice's Secret Number : " + str(s1)
print "Bob's Secret Number : " + str(s2)
