
select_form = input("encode of decode = ")

string = input("input: ")

n = int(input("aantal pos: "))

def encode(string, n):
    for i in string:
        if i > "a" or i < "z":
            res = ""
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
        if i > "a" or i < "z":
            res = ""
            ASCII = ord(i)
            f = ASCII - n
            if f < 97:
                f += 26
            letter_decode = chr(f)
            res += letter_decode
        else:
            res += i
    return res
if select_form == "encode":
    print(encode(string, n))
else:
    print(decode(string, n))
