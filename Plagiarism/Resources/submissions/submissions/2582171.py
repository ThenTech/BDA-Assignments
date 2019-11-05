def cleanup_spaces(s):
    while s[0] == " " and len(s) !=1:
        s = s[1:]
    while s[len(s)-1] == " " and len(s) != 1:
        s = s[:len(s)-1]
    while "  " in s and len(s) != 1:
        for i in range(len(s)-2):
            if s[i] == " " and s[i+1] == " ":
                s = s[0:i] + s[i+1:]
                break
    if s == " ":
        s = ""
    return s

