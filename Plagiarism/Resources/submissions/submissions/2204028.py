def convert_to_uppercase(string):
    new_string = ""
    for letter in string:
        if "a" <= letter <= "z":
            new_number = ord(letter) - ord("a") + ord("A")
            uppercase = chr(new_number)
            new_string = new_string + uppercase
        else:
            new_string = new_string + letter
    return new_string