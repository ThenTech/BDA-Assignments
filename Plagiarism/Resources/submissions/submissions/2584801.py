def encode(s, n):
    n = n % 26 
    encoded_string
    for x in s:
        if ord("a") <= (ord(x) + n) <= ord("z"):
            encoded_string += chr(ord(x) + n)
        else:
            encoded_string += ((ord(x) + n) - ord("z") + ord("a") - 1)
    return encoded_string

def decode(s, n):
    encode(s, -n)