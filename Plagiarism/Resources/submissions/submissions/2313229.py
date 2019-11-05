def cleanup_spaces(s):
    for x in range(len(s)):
        if s[x] == " " and s[x+1]!=" ":
            return s[x]
        elif s[x] != " ":
            return s[x]
