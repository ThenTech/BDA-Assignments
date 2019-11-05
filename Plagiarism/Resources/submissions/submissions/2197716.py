def encode(s, n):
    new = ""
    for i in range(len(s)):
        if s[i] == " ":
            new += " "
        else:
            character= chr(ord(s[i])+n)
            while ord(character) > 122:
                character = chr(97 +(ord(character)-122))
            new += character
    return new
print(encode("a secret message", 3))
def decode(s, n):
    new = ""
    for i in range(len(s)):
        if s[i] == " ":
            new += " "
        else:
            character = chr(ord(s[i] )-n)
            while ord(character) < 97:
                character = chr(122- (97 - ord(character)))
            new += character
    return new
print(decode('d vhfuhw phvvdjh', 3))