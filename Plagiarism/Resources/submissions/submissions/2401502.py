def convert_to_uppercase(s):
    new = ""
    for i in range(len(s)):
        if ord('a') <= ord(s[i]) <= ord('z'):
            new += chr(ord(s[i] - ord('a') + ord('A')))
        else:
            new += s[i]
    return new
