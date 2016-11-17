from random import randint

#Some code is taken,
#For example, I understand what gcd is, and how to find it.
#But a smaller, more streamline implementation made more sense

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def get_gcd(totient):
    gcd_ = []
    for i in range(1, t):
        current_coprime = gcd(i,t)
        if(current_coprime == 1):
            gcd_.append(i)
    return gcd_

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(key, totient):
    g, x, y = egcd(key, totient)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % totient

def encrypt(public, plaintext):
    generated_key, primes_multipled = (public[1], public[0])
    cipher = [(ord(char) ** generated_key) % primes_multipled for char in plaintext]
    return cipher

def decrypt(private, primes_multiplied, ciphertext):
    print private
    print primes_multiplied
    plain = [chr((char ** private) % primes_multiplied) for char in ciphertext]
    return ''.join(plain)




prime_number_a = 17
prime_number_b = 23
prime_mult = prime_number_a * prime_number_b

t = (prime_number_a - 1)*(prime_number_b - 1)
coprimes = get_gcd(t)
#print t
#print "Co Primes" + str(coprimes)

public_keys = [prime_mult, coprimes[randint(0,len(coprimes) -1)]]
private_key = modinv(public_keys[1], t)
print "Public Keys: " + str(public_keys)
print "Private Key: " + str(private_key)
encrypted_nums = encrypt(public_keys, 'Keith Kenny')
chars = decrypt(private_key, prime_mult, encrypted_nums)
print "Decoded Message: " + chars