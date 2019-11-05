def encode(s, n):
    output = ""
    for i in range(len(s)):
        output = output + encode_char(s[i])
    return output


def encode_char(c):
    if ord(c) == 32:
        return " "
    elif c >= chr(123-3):
        return chr(ord(c) - 26)
    else:
        return chr(ord(c) + 3)


print(encode("a secret message zyxw", 3))
