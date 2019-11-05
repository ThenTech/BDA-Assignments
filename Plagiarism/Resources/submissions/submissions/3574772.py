def cleanup_spaces(s):
    space = True
    output = ""
    for i in s:
        if i == ' ':
            if not space:
                output += i
        else:
            output += i
            space = False
            
    if string[len(string)-1] == " ":
        return string[:len(string)-1]
    return output
    