def encode(s, n):
    output = ""
    for i in range(len(s)):
        output += encode_char(s[i], n)
    return output


def encode_char(c, n):
    if c >= chr(ord("z") - n):
        return chr(ord(c) - 26 + n)
    else:
        return chr(ord(c) + n)


def decode(s, n):
    n = -n
    output = ""
    for i in range(len(s)):
        output += decode_char(s[i], n)
    return output


def decode_char(c, n):
    if c >= chr(ord("z") - n):
        return chr(ord(c) - 26 + n)
    else:
        return chr(ord(c) + n)
