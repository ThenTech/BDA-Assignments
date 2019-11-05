def convert_to_uppercase(s):

    uppercase = ""

    for i in range(len(s)):
        if s[i] <= "z" and s[i] >= "a":
            upper = chr(ord(s[i]) - 32)
            uppercase += upper
        else:
            uppercase += s[i]

    return uppercase