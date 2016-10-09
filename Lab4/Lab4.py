import pyDes
from Crypto.Cipher import AES
from Crypto import Random


def encrypt(key, mode, plaintext, iv=None, pad=None, cipher=None):
    if cipher == 'AES':
        return _aes_encrypt(key, mode, plaintext, pad=pad).encode('HEX').upper()
    if pad:
        plaintext = plaintext + pad

    k = pyDes.des(key, mode, IV=iv)
    encrypted_text = k.encrypt(plaintext)
    return encrypted_text.encode('HEX').upper()


def decrypt(key, mode, ciphertext, iv=None, pad=None, cipher=None):
    #if cipher == 'AES':
    #   return _aes_decrypt()

    k = pyDes.des(key, mode, IV=iv)
    decoded_cipher = ciphertext.decode('HEX')
    return k.decrypt(decoded_cipher, pad)


def _aes_encrypt(key, mode, plaintext, iv=None, pad=None):
    k = AES.new(key, mode)
    return k.encrypt(plaintext)


# Question 1
key = b"1234567812345678"
plaintext = "AAAABBBBCCCCDDDDAA"
plaintext_pad = "AAAABBBBCCCCDDDDAA\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x0014"
print encrypt(key, AES.MODE_ECB, plaintext, cipher='AES')



