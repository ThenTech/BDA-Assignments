def encode(string, rotation):
    encoded_string = ""
    for char in string:
        encoded_string += chr((ord(char) + rotation) % (26 + ord("a")))
    return encoded_string


def decode(string, rotation):
    decoded_string = ""
    for char in string:
        decoded_string += chr((ord(char) - rotation) % (26 + ord("a")))
    return decoded_string