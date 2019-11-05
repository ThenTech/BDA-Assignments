def convert_to_uppercase(s):
    lowercase = "azertyuiopqsdfghjklmwxcvbn"
    capitalised =""
    for char in s:
        if char in lowercase:
            capitalised += chr(ord(char)-32)
        else:
            capitalised += char
    return capitalised