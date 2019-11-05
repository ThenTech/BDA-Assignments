def cleanup_spaces(s):
    string = ""
    for i in range(len(s)):
        if s[i]==0:
            if i != " ":
                string += s[i]
        elif s[i] == " "and s[i-1]!= " ":
            string += s[i]
        elif s[i] != " ":
            string += s[i]
    if len(string) == 0:
        return string
    else:
        if string[len(string)-1]==" ":
            return string[:len(string)-1]
    return string        
    