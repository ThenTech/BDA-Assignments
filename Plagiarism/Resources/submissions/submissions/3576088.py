def encode(string, n):
    while n > 26:
        n -= 26
    while n < 0:
        n += 26

    output = ""
    for i in string:
        if i.isalpha():
            buffer = ord(i) + n
            if buffer > (ord('z')):
                buffer -= 26
            if buffer > ord('Z') and buffer < ord('a'):
                buffer -= 26
            output += chr(buffer)
        else:
            output += i
    return output


def decode(s, n):
    return encode(s, -n)