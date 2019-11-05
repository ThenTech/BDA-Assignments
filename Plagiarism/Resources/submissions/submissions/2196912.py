def cleanup_spaces(s):
    newword = ""
    for i in range(len(s)):
        if 97 <= ord(s[i]) and ord(s[i]) <= 122:
            newword += chr(ord[i]+26)
        else:
            newword += s[i]
    return newword