def encode(string, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for i in string:
        if i in alphabet:
            ASCII = ord(i)
            f = ASCII + n
            if f > 122:
                f -= 26
            elif f < 97:
                f += 26
            letter_encode = chr(f)
            res += letter_encode
            f = 0
        else:
            res += i
    return res

def decode(string, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for i in string:
        if i > "a" in alphabet:
            ASCII = ord(i)
            f = ASCII - n
            if f < 97:
                f += 26
            elif f > 122:
                f -= 26
            letter_decode = chr(f)
            res += letter_decode
            f = 0
        else:
            res += i
    return res