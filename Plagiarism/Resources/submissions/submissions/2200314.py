def cleanup_spaces(s):
    word = ""
    i = 0
    while i < len(s):
        if s[i] != " ":
            word += s[i]
            count = 0
        elif s[i] == " " and len(word) != 0:
            count = 1
            if i+1 < len(s)-1 and s[i+1] != " " and count == 1:
                word += " "
        i += 1
    return word
    