def cleanup_spaces(s):
    zin = ""
    for i in range(len(s)):
        if s[i] != " ":
            zin =zin + s[i]
        elif s[i-1] != " " and i != len(s)-1:
            zin = zin + s[i]
    return zin
print(cleanup_spaces("   Deze    zin   is   test "))