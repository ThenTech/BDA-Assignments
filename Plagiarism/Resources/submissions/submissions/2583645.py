def cleanup_spaces(s):
    spatie = False
    x = ""
    i = 0
    while i < len(s):
        if s[0] == " ":
            spatie = True
            i += 1
        if s[i] != " ":
            x += s[i]
            spatie = False
            i += 1
        else:
            if not spatie:
                x += s[i]
                spatie = True
                i += 1
            
            