def cleanup_spaces(s):
    delspace = False
    x = 0
    end = False
    while not end:
        if s[x]==' ' and delspace:
            s = s[:x] + s[x+1:]
            x -= 1
            delspace = True
        elif s[x]==' ' and not delspace:
            delspace = True
        elif not s[x]==' ':
            delspace = False

        x += 1
        if x >= len(s):
            end = True
    if s[0] == ' ':
        s = s[1:]
    if s[len(s)-1] == ' ':
        s = s[:len(s)-1]
    return s
