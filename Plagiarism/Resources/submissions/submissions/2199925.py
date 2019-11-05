def encode(s, n):
    encoded = ""

    if n > 26:
        n -= 26
    if n < -26:
        n += 26

    for i in s:
        if 97 <= ord(i) <= 122:
            inAlphabet = ord(i) + n
            if inAlphabet > ord('z'):
                inAlphabet -= 26
            if inAlphabet < ord('a'):
                inAlphabet += 26
            encoded += chr(inAlphabet)
        else:
            encoded += i

    return encoded


def decode(s, n):
    decoded = ""
    if n > 26:
        n -= 26

    if n < -26:
        n += 26

    for i in s:
        if 97 <= ord(i) <= 122:
            inAlphabet = ord(i) - n
            if inAlphabet > ord('z'):
                inAlphabet -= 26
            if inAlphabet < ord('a'):
                inAlphabet += 26
            decoded += chr(inAlphabet)
        else:
            decoded += i
    return decoded
