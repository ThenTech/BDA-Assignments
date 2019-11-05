def convert_to_uppercase(s):
    newstring = ""
    for character in s:
        if "a" <= character <= "z":
            upper_version = chr(ord("A") + ord(character) - ord("a"))
            newstring += upper_version
        else:
            newstring += character
    return newstring
            