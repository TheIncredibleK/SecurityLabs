import binascii
from Crypto.Cipher import AES

def addpadding(plain_text_unpadded, size=16):
    padding = ''
    if (len(plain_text_unpadded) > size):
        empty_pieces = size - len(plain_text_unpadded) % 8 - 2
    else:
        empty_pieces = size - len(plain_text_unpadded) - 2

    for i in range(0, empty_pieces):
        padding += '\x00'

    padding +=  str((size - len(plain_text_unpadded) % size))
    return plain_text_unpadded + padding

def removepadding(plain_text_padded):
    empty_loc = plain_text_padded.find('\x00')
    plaintext_unpadded = plain_text_padded[:empty_loc]
    return plaintext_unpadded

def encrypt(key, plaintext):
    plaintext = addpadding(plaintext)
    cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return binascii.hexlify(bytearray(ciphertext))

def decrypt(key, ciphertext):
    ciphertext = binascii.unhexlify(ciphertext)
    cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
    ciphertext = removepadding(cipher.decrypt(ciphertext))
    return ciphertext

key_ = "1234567812345678"
plaintext = "AAAABBBBCCCCDDDDAA"
encrypted_text = encrypt(key_, plaintext)
print "Question 1:"
print(encrypted_text.upper())
decrypted_text = decrypt(key_, encrypted_text)
print(decrypted_text)


print "\nQuestion 2:"
question2_encrypted = encrypt("1234567812345678", "AAAABBBBCCCCDDDDAA")

with open('libraryfile.txt', 'r') as lib:
    for line in lib.readlines():
        attempted_decrypt = decrypt(line.rstrip(), question2_encrypted)
        if attempted_decrypt == "AAAABBBBCCCCDDDDAA":
            print "KEY", line.rstrip()

