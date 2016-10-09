from itertools import cycle
alphabet = "abcdefghijklmnopqrstuvwxyz"

def vignere(text, key):
    result=""
    text = ''.join(text)
    new_text = text.replace(" ", "").lower()
    new_text = [i for i in new_text if i in alphabet]
    letter_to_key = zip(new_text, cycle(key))

    for text_letter, key_letter in letter_to_key:
        if text_letter in alphabet:
            result += reduce(lambda text_, key_: alphabet[(alphabet.index(text_) + alphabet.index(key_)) % 26], text_letter, key_letter)
        else:
            result += text_letter

    return result

def decrypt_vignere(text, key):
    result = ""
    text = ''.join(text)
    new_text = text.replace(" ", "").lower()
    new_text = [i for i in new_text if i in alphabet]
    letter_to_key = zip(new_text, cycle(key))

    for text_letter, key_letter in letter_to_key:
        if text_letter in alphabet:
            result += alphabet[(alphabet.index(text_letter) - alphabet.index(key_letter)) % 26]
        else:
            result += text_letter

    return result

