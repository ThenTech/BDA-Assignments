def encode(s, n):
    encoded =""
    for i in s:
        if 97 <= ord(i) <= 122:
            ascii_number = (ord(i) + n)
            while ascii_number > 122:
                ascii_number = ascii_number - 26
            encoded += chr(ascii_number)
        else:
            encoded += i
    return encoded

def decode(s, n):
    encoded = ""
    for i in s:
        if 97 <= ord(i) <= 122:
            ascii_number = (ord(i) - n)
            while ascii_number < 97:
                ascii_number = ascii_number + 26
            encoded += chr(ascii_number)
        else:
            encoded += i
    return encoded