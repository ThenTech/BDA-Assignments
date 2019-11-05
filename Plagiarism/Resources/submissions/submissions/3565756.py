def convert_to_uppercase(s):
    out = ""
    length = len(s)
    for i in range(length):
        if ord('a') <= ord(s[i]) <= ord('z'):
            letter = chr(ord(s[i])-32)
            out += letter
        else:
            out += s[i]
    return out