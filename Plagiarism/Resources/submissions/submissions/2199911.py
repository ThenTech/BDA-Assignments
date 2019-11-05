def cleanup_spaces(s):
    s = s.split()
    x = ''

    for i in s:
        x += i
        if i != s[len(s)-1]:
            x += ' '
    return x