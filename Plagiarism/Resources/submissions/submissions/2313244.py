def cleanup_spaces(s):
    newstring = ""
    for x in range(len(s)):
        if s[x] == " " and s[x+1]!=" ":
            newstring += s[x]
        elif s[x] != " ":
            newstring += s[x]
    return newstring        
