def encode(string, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_string = ""
    for char in string:
        if char in alphabet:
            new_ord = ord(char) + n

            while new_ord > 122:
                new_ord -= 26
            while new_ord < 97:
                new_ord += 26

            encoded_string += chr(new_ord)
        else:
            encoded_string += char

    return encoded_string

def decode(string, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_string = ""
    for char in string:
        if char in alphabet:
            new_ord = ord(char) - n

            while new_ord < 97:
                new_ord += 26
            while new_ord > 122:
                new_ord -= 26

            decoded_string += chr(new_ord)
        else:
            decoded_string += char

    return decoded_string