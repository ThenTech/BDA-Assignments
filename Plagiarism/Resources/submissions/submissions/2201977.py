def cleanup_spaces(s):
    words = ""
    word = ""
    s += "  "
    for i in s:
        if i != " ":
            word += i
        else:
            if word != "":
                words += word + " "
                word = ""

    return (words)