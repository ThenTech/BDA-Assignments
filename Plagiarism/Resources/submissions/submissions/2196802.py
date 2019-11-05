alphabet = "abcdefghijklmnopqrstuvwxyz"


def encode(s, n):
    output = ""
    for i in s:
        place = alphabet.find(i) + n
        output += alphabet[place % len(alphabet)]
    return output


def decode(s, n):
    return encode(s, -n)
