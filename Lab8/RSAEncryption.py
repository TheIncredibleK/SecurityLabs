from random import randint


def greated_common_divisor(number_a, number_b):
    while number_b != 0:
        number_a, number_b = number_b, number_a % number_b
    return number_a

def get_gcd(totient):
    gcd_ = []
    for i in range(1, t):
        current_coprime = greated_common_divisor(i, t)
        if(current_coprime == 1):
            gcd_.append(i)
    return gcd_

def extended_greated_common_div(number_a, number_b):
    if number_a == 0:
        return (number_b, 0, 1)
    else:
        greatest_com_div, number_c, number_d = extended_greated_common_div(number_b % number_a, number_a)
        return (greatest_com_div, number_d - (number_b // number_a) * number_c, number_c)

def modular_inverse(key, totient):
    greatest_com_div, number_c, number_d = extended_greated_common_div(key, totient)
    return number_c % totient

def encrypt(public, plaintext):
    generated_key, primes_multipled = (public[1], public[0])
    cipher = [(ord(char) ** generated_key) % primes_multipled for char in plaintext]
    return cipher

def decrypt(private, primes_multiplied, ciphertext):
    plain = [chr((char ** private) % primes_multiplied) for char in ciphertext]
    return ''.join(plain)




prime_number_a = 17
prime_number_b = 23
prime_mult = prime_number_a * prime_number_b

t = (prime_number_a - 1)*(prime_number_b - 1)
coprimes = get_gcd(t)
print "Co Primes" + str(coprimes)

public_keys = [prime_mult, coprimes[randint(0,len(coprimes) -1)]]
private_key = modular_inverse(public_keys[1], t)
print "Public Keys: " + str(public_keys)
print "Private Key: " + str(private_key)
encrypted_nums = encrypt(public_keys, 'Keith Kenny')
print encrypted_nums
chars = decrypt(private_key, prime_mult, encrypted_nums)
print "Decoded Message: " + chars