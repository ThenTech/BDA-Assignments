def convert_to_uppercase(s):
    newstring = ""
    for i in range(len(s)):
        if "a" <= s[i] <= "z":
            temp = ord(s[i])
            temp = temp - 32
            upper = chr(temp)
            newstring += upper
        else:
            newstring += s[i]
    return newstring