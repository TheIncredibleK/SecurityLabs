from Crypto.Hash import SHA256

hasher = SHA256.new()

to_hash = "AAABBBCCCD"
hasher.update(to_hash)
print hasher.digest().encode("HEX").upper()