import string

def encode(s, m):
    for i in range(len(s)):
        if ord(s[i]) == 32:
            print(" ", end="")
        else:
            x = ord(s[i]) + m
            print(chr(x), end="")
    return ""

print(encode("a bb c", 3))
