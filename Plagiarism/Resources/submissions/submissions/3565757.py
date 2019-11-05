def encode(s, n):
    out = ""
    length = len(s)
    for i in range(length):
        if s[i] == " ":
            out += " "
            continue
        letter = chr(ord(s[i]) + n)
        out += letter
    return out



def decode(s, n):
    pass