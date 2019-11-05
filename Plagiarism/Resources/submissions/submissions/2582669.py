def encode(s, n):
    encoded =""
    for i in s:
        ascii_number = (ord(i) + n)
        while ascii_number > 122:
            ascii_number = ascii_number - 26
        encoded += chr(ascii_number)

def decode(s, n):
    encoded = ""
    for i in s:
        ascii_number = (ord(i) - n)
        while ascii_number < 97:
            ascii_number = ascii_number + 26
        encoded += chr(ascii_number)