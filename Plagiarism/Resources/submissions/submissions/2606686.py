def convert_to_uppercase(string):
    uppercase_string = ""
    z = 0
    for i in string:
        if "a" <= i <= "z":
            z = ord(str(i))
            z = int(z) - 32
            z = chr(int(z))
            uppercase_string += z
        else:
            uppercase_string += i
    return uppercase_string