def convert_to_uppercase(string):
    return_string = ""
    offset = ord("a") - ord("A")

    for char in string:
        if "a" <= char <= "z":
            return_string += chr(ord(char) + offset)
        else:
            return_string += char
    
    return return_string
