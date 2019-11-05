def cleanup_spaces(s):
    new = ""
    for i in range(len(s)):
        if s[i] == ' ':
            if i != len(s) - 1 and s[i+1] != ' ' and new != "":
                new += s[i]
        else:
            new += s[i]
    return new