def cleanup_spaces(s):
    while "  " in s:
        for i in range(len(s) - 1):
            if s[i] == " " and s[i + 1] == " ":
                s = s[:i] + s[i+1:]
                break
    return s