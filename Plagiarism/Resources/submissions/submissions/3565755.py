def cleanup_spaces(s):
    new_string = s.split()
    length = len(new_string)
    out = ""
    for word in range(length):
        out += new_string[word]
        if word != len(new_string)-1:
            out += " "
    return out