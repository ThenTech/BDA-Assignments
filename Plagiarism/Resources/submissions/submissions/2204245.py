def convert_to_uppercase(string):
    nieuwe_string = ""
    for el in string:
        if ord(a)<= el <= ord(z):
            nieuwe_string = nieuwe_string + el
        else:
            ord(el) = ord(el)-32
            nieuwe_string = nieuwe_string + el
    return nieuwe_string
