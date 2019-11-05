def cleanup_spaces(s):
    a=""
    for i in s:
        if i not in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN":
            a+=i
        elif ord(i)-97<0:
            a+=i
        else:
            cijfer=ord(i)
            a+=chr(cijfer-32)
    return a