def cleanup_spaces(s):
    string = ""
    for i in range(len(s)-1):
        if i=0:
            pass
        elif s[i] == " "and s[i-1]!= " ":
            string += s[i]
        elif s[i] != " ":
            string += s[i]
    if string[len(string)-1]==" ":
        return string[len(string)-2]
    return string        
    