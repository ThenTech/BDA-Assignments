import string

def encode(s, move):
    for i in range(len(s)):
        if ord(s[i]) == 32:
            print(chr(s[i]), end ="")
        else:
            x = ord(s[i]) + move
            print(chr(x), end = "")
    print()

print(encode("aabbbdfd", 3))