def encode(string, n):
    for i in string:
        res = ""
        if i > "a" or i < "z":
            ASCII = ord(i)
            f = ASCII + n
            if f > 122:
                f -= 26
            letter_encode = chr(f)
            res += letter_encode
        else:
            res += i
    return res

def decode(string, n):
    for i in string:
        res = ""
        if i > "a" or i < "z":
            ASCII = ord(i)
            f = ASCII - n
            if f < 97:
                f += 26
            letter_decode = chr(f)
            res += letter_decode
        else:
            res += i
    return res