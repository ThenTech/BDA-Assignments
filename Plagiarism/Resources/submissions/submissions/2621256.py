def encode(string, number):
    coded_string = ""
    for i in string:
        if 97 < ord(i) < 122:
            new_value = ord(i) + number
            while new_value > 122:
                new_value = new_value - 26
            while new_value < 97:
                new_value = new_value + 26
            coded_string += chr(new_value)
        else:
            coded_string += i
    return coded_string

def decode(string, number):
    coded_string = ""
    for i in string:
        if 97 < ord(i) < 122:
            new_value = ord(i) - number
            while new_value > 122:
                new_value = new_value - 26
            while new_value < 97:
                new_value = new_value + 26
            coded_string += chr(new_value)
        else:
            coded_string += i
        return coded_string