import binascii
from Crypto.Cipher import AES

BLOCK_SIZE = 16

# __ to specify a function that will only be called from within another function
def __pad(raw):
    padding = ''
    if (len(raw) > BLOCK_SIZE):
        nulls = BLOCK_SIZE - len(raw) % 8 - 2
    else:
        nulls = BLOCK_SIZE - len(raw) - 2

    for i in range(0, nulls):
        padding += '\x00'

    padding +=  str((BLOCK_SIZE - len(raw) % BLOCK_SIZE))
    # this is the calculated padding
    return raw+padding

def __unpad(s):
    # This removes the trailing characters/padding
    ind = s.find('\x00')
    plain = s[:ind]
    return plain

def encrypt(key, raw):
    # Takes in a string of text and encrypts it.
    # padding put on before sent for encryption
    raw = __pad(raw)
    cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
    ciphertext = cipher.encrypt(raw)
    # changes the ciphertext into hex then decodes it into utf-8
    return binascii.hexlify(bytearray(ciphertext))

def decrypt(key, enc):
    # Takes in a string of ciphertext and decrypts it.
    enc = binascii.unhexlify(enc)
    cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
    enc = __unpad(cipher.decrypt(enc))
    return enc

# 43D3215C92A75A1478FCF9CB950D20DB502A485FD5735486D57AEA9AA809E3DD
enc = encrypt("1234567812345678","AAAABBBBCCCCDDDDAA")
# opens library file in read mode then goes through each line checking if plaintext is the same
f = open('libraryfile.txt', 'r')
for line in f:
    # rstrip() removes the carraige return
    dec = decrypt(line.rstrip(), enc)
    if dec == "AAAABBBBCCCCDDDDAA":
        print "The key is", line.rstrip()
#         output The key is 1234567812345678

