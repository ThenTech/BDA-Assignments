def encode(string, n):
    new_string = ""
    for letter in string:
        number = ord(letter)
        new_number = number + n
        if new_number < 97 or new_number > 123:
            new_string = new_string + letter
            continue
        if new_number > 122:
            new_number = new_number - 27
            new_letter = chr(new_number)
            new_string = new_string + new_letter
        else:
            new_letter = chr(new_number)
            new_string = new_string + new_letter
    return new_string

def decode(string, n):
    old_string = ""
    for letter in string:
        number = ord(letter)
        old_number = number - n
        if old_number < 97:
            old_number = old_number + 27
            old_letter = chr(old_number)
            old_string = old_string + old_letter
        else:
            old_letter = chr(old_number)
            old_string = old_string + old_letter
    return old_string

