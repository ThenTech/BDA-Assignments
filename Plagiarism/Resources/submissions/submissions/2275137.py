def encode(s, n):
    for i in s:
        a = ord(i)
        b = a + n
        if a < 97:
            print(chr(a), end="")
        elif b > 122:
            c = (b - 122 + 96)
            print(chr(c), end="")
        elif b < 97:
            d = (b +26)
            print(chr(d), end="")
        else:
            print(chr(b), end="")
    print()

def decode(s, n):
    for i in s:
        a = ord(i)
        b = a - n
        if a < 97:
            print(chr(a), end="")
        elif b < 97:
            c = (b +26)
            print(chr(c), end="")
        elif b > 122:
            d = (b - 122 + 96)
            print(chr(d), end="")
        else:
            print(chr(b), end="")
    print()