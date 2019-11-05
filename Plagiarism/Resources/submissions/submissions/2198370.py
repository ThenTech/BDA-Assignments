def cleanup_spaces(string):
    upper_string = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in string:
        if char in alphabet:
            higher_ord = ord(char) + 32
            upper_string += chr(higher_ord)
        else:
            upper_string += char
    return upper_string