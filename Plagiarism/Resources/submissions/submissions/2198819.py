def encode(string, n):
    encoded_string = ""
    for char in string:
        new_ord = ord(char) + n
        if new_ord > 122:
            new_ord -= 25
        encoded_string += chr(new_ord)

def decode(string, n):
    decoded_string = ""
    for char in string:
        new_ord = ord(char) - n
        if new_ord < 97:
            new_ord += 25
        decoded_string += chr(new_ord)