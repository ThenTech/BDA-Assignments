def cleanup_spaces(s):
    newstring = ""
    for x in range(len(s)):
        if x <= len(s)-1:
            if s[x] == " " and s[x+1]!=" ":
                newstring += s[x]
        if s[x] != " ":
            newstring += s[x]
    return newstring        
