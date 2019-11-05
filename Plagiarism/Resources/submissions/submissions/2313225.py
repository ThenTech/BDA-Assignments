def cleanup_spaces(s):
    for x in range(len(s)):
        if s[x] == " " and s[x+1]!=" ":
            print(s[x], end="")
        elif s[x] != " ":
            print(s[x], end="")
