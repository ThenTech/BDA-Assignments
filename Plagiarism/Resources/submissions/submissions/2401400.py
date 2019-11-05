def cleanup_spaces(s):
    new = ""
    for i in range(len(s)):
        if s[i] == ' ':
            if s[i-1] != ' ' and i != 0 and i != len(s) - 1:
                new += s[i]
        else:
            new += s[i]
    return new
