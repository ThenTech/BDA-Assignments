def encode(string, n):
    new_string = ""
    division = (n // 27)
    i = 1
    if n < 0:
        i = -1
    for letter in string:
        number = ord(letter)
        new_number = number + n
        if number < 97 or number > 123:
            new_string = new_string + letter
            continue
        if new_number > 122 + (division * 26) or new_number < 97 + (division * 26):
            new_number = new_number - (26 * i * division)
        if new_number > 122 or new_number < 97:
            new_number = new_number - (26 * i)
            new_letter = chr(new_number)
            new_string = new_string + new_letter
        else:
            new_letter = chr(new_number)
            new_string = new_string + new_letter
    return new_string

def decode(string, n):
    old_string = ""
    division = (n // 27)
    i = 1
    if n < 0:
        i = 1
    for letter in string:
        number = ord(letter)
        old_number = number - n
        if number < 97 or number > 123:
            old_string = old_string + letter
            continue
        if old_number < 97 - (division * 26):
            old_number = old_number + (26 * i * division)
        if old_number < 97:
            old_number = old_number + (26 * i)
            old_letter = chr(old_number)
            old_string = old_string + old_letter
        else:
            old_letter = chr(old_number)
            old_string = old_string + old_letter
    return old_string