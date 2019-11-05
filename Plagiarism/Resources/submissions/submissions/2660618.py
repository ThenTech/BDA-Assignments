def cleanup_spaces(s):
    while s[0] == " " and len(s)>= 1:
        s = s[1:]
    while s[len(s)-1] == " " and len(s)>= 1:
        s = s[:len(s)-1]
    while "  " in s:
        for i in range(len(s)):
            if s[i] == " " and s[i+1] == " " and i < len(s) -1:
                s = s[:i] + s[i+1:]
                break
    return s
            