def convert_to_uppercase(s):
    upper = ""
    for letter in s:
        if ord("a") <= ord(letter) <= ord("z"):
            upper += chr(ord(letter) - (ord("a") - ord("A")))
    return upper