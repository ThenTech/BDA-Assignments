def encode(s, n):
    new = ""
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(s)):
        if s[i] not in alphabet:
            new += s[i]
        else:
            character= chr(ord(s[i])+n)
            while ord(character) > 122:
                character = chr(97 +(ord(character)-122))
            while ord(character) < 97:
                character = chr(122-(96-ord(character)))
            new += character
    return new
print(encode("be positive, not negative!", 26))
def decode(s, n):
    new = ""
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(s)):
        if s[i] not in alphabet:
            new += s[i]
        else:
            character = chr(ord(s[i] )-n)
            while ord(character) < 97:
                character = chr(122- (97 - ord(character)))
            new += character
    return new
print(decode('d vhfuhw phvvdjh', 3))