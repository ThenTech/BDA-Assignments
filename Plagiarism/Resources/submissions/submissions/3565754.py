def cleanup_spaces(s):
    new_string = s.split()
    out = ""
    for word in range(len(new_string)):
        out += new_string[word]
        if word != len(new_string)-1:
            out += " "
    return out