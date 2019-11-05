def cleanup_spaces(s):
    space = True
    output = ""
    for i in s:
        if i == ' ':
            if not space:
                output += i
        else:
            output += i
        if not i.isalpha() and i != ' ':
            break
    return output
    