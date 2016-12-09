from random import randint
from math import pow

def get_roots():
    def greatest_common_divisor(number_a, number_b):
        while number_b != 0:
            number_a, number_b = number_b, number_a % number_b
        return number_a

    def get_primitive_roots(wanted_mod):
        roots = []
        necessary_numbers = set(integer for integer in range (1, wanted_mod) if greatest_common_divisor(integer, wanted_mod) == 1)

        for each_mod in range(1, wanted_mod):
            the_set = set(pow(each_mod, each_power) % wanted_mod for each_power in range (1, wanted_mod))
            if necessary_numbers == the_set:
                roots.append(each_mod)
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
