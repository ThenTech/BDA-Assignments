def is_lowercase_letter(ch):
    return "a" <= ch <= "z"
    

def cleanup_spaces(s):
    new_string = ""
    for char in s:
        if is_lowercase_letter(char):
            letter = chr(ord(char) - 32)
            newstring += letter
        else:
            new_string += char
    return new_string