import pyDes

def encrypt(key, mode, plaintext, iv=None, pad=None):
    if pad:
        plaintext = plaintext + pad

    k = pyDes.des(key, mode, IV=iv)
    encrypted_text = k.encrypt(plaintext)
    return encrypted_text.encode('HEX').upper()


def decrypt(key, mode, ciphertext, iv=None, pad=None):
    k = pyDes.des(key, mode, IV=iv)
    decoded_cipher = ciphertext.decode('HEX')
    return k.decrypt(decoded_cipher, pad)

print "Question 1 \n"
# Question 1
key = "12345678"
the_mode = pyDes.ECB
plaintext = "AAAABBBBAAAABBBB"
ciphertext = "19FF4637BB2FE77C19FF4637BB2FE77C"

print encrypt(key, the_mode, plaintext)
print decrypt(key, the_mode, ciphertext)

print "\nQuestion 2\n"
# Question 2
key = "12345678"
iv = "00000000"
the_mode = pyDes.CBC
plaintext = "AAAABBBBAAAABBBB"
ciphertext = "AAC823F6BBE58F9EAF1FE0EB9CA7EB08"

print encrypt(key, the_mode, plaintext, iv=iv)
print decrypt(key, the_mode, ciphertext, iv=iv)

print "\nQuestion 3\n"
# Question 3
key = "12345678"
plaintext = "AAAABBBBCCCC"
padding = '\x00\x0004'
ciphertext = "19FF4637BB2FE77C81987E5CB99B66E2"
the_mode = pyDes.ECB
pad_mode = pyDes.PAD_NORMAL

print encrypt(key, the_mode, plaintext, pad=padding)
print decrypt(key, the_mode, ciphertext, pad=padding)
