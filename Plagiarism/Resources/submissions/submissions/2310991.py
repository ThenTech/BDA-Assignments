def encode(string, n):
    res = ""
    for i in string:
        if i > "a" or i < "z":
            ASCII = ord(i)
            f = ASCII + n
            if f > 122:
                f -= 26
            letter_encode = chr(f)
            res += letter_encode
            f = 0
        else:
            res += i
    return res

def decode(string, n):
    res = ""
    for i in string:
        if i > "a" or i < "z":
            ASCII = ord(i)
            f = ASCII - n
            if f < 97:
                f += 26
            letter_decode = chr(f)
            res += letter_decode
            f = 0
        else:
            res += i
    return res