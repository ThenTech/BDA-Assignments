def convert_to_uppercase(s):
    newword = ""
    for i in range(len(s)):
        if 97 <= ord(s[i]) and ord(s[i]) <= 122:
            number = ord("A") + (ord(s[i]) - ord("a")) 
            newword += chr(number)
        else:
            newword += s[i]
    return newword