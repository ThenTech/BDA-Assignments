def cleanup_spaces(s):
    s = s.split()
    output = ""
    for i in range(len(s)):
        output += s[i]
        if i < len(s) - 1:
            output += " "
    return output
