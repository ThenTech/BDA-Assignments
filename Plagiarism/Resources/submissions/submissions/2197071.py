def convert_to_uppercase(s):
    newword = ""
    for i in range(len(s)):
        if 97 <= ord(s[i]) and ord(s[i]) <= 122:
            newword += chr(ord(s[i])+26)
        else:
            newword += s[i]
    return newword