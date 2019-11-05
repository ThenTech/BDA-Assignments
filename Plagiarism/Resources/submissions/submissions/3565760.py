def shifter(s, n):
    out = ""
    for char in s:
        if 'a' <= char <= 'z':
            number = ord(char) - ord('a')
            number = (number + n) % 26
            out += chr(number + ord('a'))
        else:
            out += char
    return out


def encode(s, n):
    out = shifter(s, n)
    return out


def decode(s, n):
    out = shifter(s, -n)
    return out