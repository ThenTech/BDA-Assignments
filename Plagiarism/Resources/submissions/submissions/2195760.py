import string


def encode(s, n):
    if n < 0:
        n = 26+n
    output = ""
    for i in range(len(s)):
        if s[i] in string.ascii_letters:
            output += encode_char(s[i],n)
        else: output += s[i]
    return output


def encode_char(c, n):
    if c <= chr(ord("z") - n):
        return chr(ord(c) + n)
    else:
        return chr(ord(c) - 26 + n)


def decode(s, n):
    if n < 0:
        n = 26+n
    output = ""
    for i in range(len(s)):
        if s[i] in string.ascii_letters:
            output += decode_char(s[i], n)
        else:
            output += s[i]
    return output


def decode_char(c, n):
    if c >= chr(ord("a") + n):
        return chr(ord(c) - n)
    else:
        return chr(ord(c) + 26 - n)