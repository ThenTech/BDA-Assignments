def replace(pattern, replacement, corpus):
    check = ""
    word = pattern
    count = 0
    for x in range(0, len(corpus)):

        y = len(pattern)
        if corpus[x:x+y] == pattern:
            for k in replacement:
                check += k
                count = len(pattern)-1
        elif count == 0:
            check += corpus[x]
        else:
            count -= 1
    return check