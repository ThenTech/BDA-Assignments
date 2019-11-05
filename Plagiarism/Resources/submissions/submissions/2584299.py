def convert_to_uppercase(s):
    new_string = ""
    for character in s:
        if "a" <= character <= "z":
            upper_version = chr(ord("A") + ord(char) - ord("a"))
            newstring += upper_version
        else:
            newstring += character
    return newstring
            