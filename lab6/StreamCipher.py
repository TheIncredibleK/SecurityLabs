from Crypto.Cipher import ARC4

key = '123456'
encryption = ARC4.new(key)
decryption = ARC4.new(key)
plain_text = "keith kenny"
cipher_text = encryption.encrypt(plain_text)
decrypted_cipher = decryption.decrypt(cipher_text)
print cipher_text.encode("hex")
print decrypted_cipher