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

def encode(letter, public_key):
    letter_num  = (ord(letter) - ord('a')) + 1
    new_letter = (letter_num**public_key[1])%public_key[0]
    return chr(new_letter + ord('a') - 1)

def decode(letter):
    return ord(letter)



prime_number_a = 17
prime_number_b = 23
prime_mult = prime_number_a * prime_number_b

t = (prime_number_a - 1)*(prime_number_b - 1)
coprimes = get_gcd(t)
#print t
#print "Co Primes" + str(coprimes)

public_keys = [t, coprimes[randint(0,len(coprimes) -1)]]
private_key = modinv(public_keys[1], t)
print public_keys
print private_key
base_n = ord('a')
end_n = ord('z')
#print encode('', public_keys)