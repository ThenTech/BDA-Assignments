def cleanup_spaces(s):
    word = ""
    i = 0
    while i < len(s):
        if s[i] != " ":
            word += s[i]
            count = 0
        elif s[i] == " ":
            count = 1
            if s[i+1] != " " and count == 1:
                word += " "
        i += 1
    return word