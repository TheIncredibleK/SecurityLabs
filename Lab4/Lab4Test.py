import pyaes

# Any mode of operation can be used; for this example CBC
key ="1234567812345678"
iv = "InitializationVe"
plaintext = "AAAABBBBCCCCDDDDAA"
plaintext_pad = "AAAABBBBCCCCDDDDAA\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x0014"
ciphertext = ''

# We can encrypt one line at a time, regardles of length
encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationECB(key))

ciphertext += encrypter.feed(plaintext_pad)

print 1
# Make a final call to flush any remaining bytes and add paddin
ciphertext += encrypter.feed()

# We can decrypt the cipher text in chunks (here we split it in half)
decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationECB(key, iv))
decrypted = decrypter.feed(ciphertext[:len(ciphertext) / 2])
decrypted += decrypter.feed(ciphertext[len(ciphertext) / 2:])

# Again, make a final call to flush any remaining bytes and strip padding
decrypted += decrypter.feed()

print file('/etc/passwd').read() == decrypted