alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "password"
text = "This is my secret"
def encryption(text, key):
    new = ""
    count = 0
    for char in text:
        key_char = key[count%len(key)].lower()
        key_index = alphabet.index(key_char)
        if char == " ":
            newchar = " "
            new += newchar
        else:
            text_index = alphabet.index(char.lower())
            newchar = alphabet[(text_index + key_index)%len(alphabet)]
            new += newchar
        count += 1
    return new

def decryption(text, key):
    new = ""
    count = 0
    for char in text:
        key_char = key[count%len(key)].lower()
        key_index = alphabet.index(key_char)
        if char == " ":
            newchar = " "
            new += newchar
        else:
            text_index = alphabet.index(char.lower())
            newchar = alphabet[(text_index - key_index)%len(alphabet)]
            new += newchar
        count += 1
    return new

encrypted = encryption(text, key)
print (encrypted)

decrypted = decryption(encrypted, key)
print (decrypted)
