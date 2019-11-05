import string


def encode(s, n):
    code = ""
    for letter in s:
        if letter in string.ascii_letters:
            if ord("a") <= ord(letter) + n <= ord("z"):
                code += chr(ord(letter) + n)
            elif ord("z") < ord(letter) - n:
                code += chr(ord(letter) - 26 + n)
        else:
            code += letter
    return code


def decode(s, n):
    pass