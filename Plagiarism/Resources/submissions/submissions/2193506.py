def cleanup_spaces(s):
    output = ""
    for i in range(len(s)-1):
        if s[i] == " ":
            if not s[i+1] == " ":
                output += " "
        else:
            output += s[i]
    return output
