string = input("input: ")
n = int(input("aantal pos: "))
def encode(string, n):
    for i in string:
        i = letter
        res = ""
        ASCII = ord(letter)
        f = ASCII + n
        if f > 122:
            f -= 26
            letter_encode = chr(f)
            res += letter encode
    return res

def decode(string, n):
    for i in string:
        i = letter
        res =""
        ASCII = ord(letter)
        f = ASCII - n
        if f < 97:
            f += 26
        letter_decode = chr(f)
        res += letter_decode
    return res
if string == "encode":
    print(encode(string, n))
else:
    print(decode(string, n))