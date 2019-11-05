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
            
    if output[len(output)-1] == " ":
        return output[:len(output)-1]
    return output
    