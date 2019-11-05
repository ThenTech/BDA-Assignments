def cleanup_spaces(s):
    list_s = s.split()
    new_s = ''
    for i in list_s:
        new_s += i + ' '
    return new_s[:len(new_s)-2]