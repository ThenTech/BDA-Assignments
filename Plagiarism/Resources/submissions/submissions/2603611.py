def cleanup_spaces(s):
    current = ""
    space = False
    for i in s:
        if i != " ":
            current += i
            space = False
        elif i == " " and not(space) and len(current) != 0:
            current += i
            space = True
        elif i == " " and space:
            continue
    return current