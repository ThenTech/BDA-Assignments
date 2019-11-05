alphabet = "abcdefghijklmnopqrstuvwxyz"


def encode(s, n):
    output = ""
    for i in s:
        if i in alphabet:
            place = alphabet.find(i) + n
            output += alphabet[place % len(alphabet)]
        else:
            output += i
    return output


def decode(s, n):
    return encode(s, -n)
