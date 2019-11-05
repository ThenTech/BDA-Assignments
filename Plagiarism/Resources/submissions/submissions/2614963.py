def encode(s, n):
    string = ""
    for i in s:
        if "a" <= i <= "z":
            cijfer = ord(i) + n
            while ord("z") < cijfer:
                cijfer -= 26
            while ord("a") > cijfer:
                cijfer += 26
            letter = chr(cijfer)
            string += letter
        else:
            string += i
    return string

def decode(s, n):
    return encode(s, -n)