def replace(pattern, replacement, corpus):
    x = ""
    i = 0
    while i < len(corpus):
        slice = corpus[i:i+len(pattern)]
        if slice != pattern:
            x += corpus[i]
            i += 1
        else:
            x += replacement
            i += len(pattern)
    return x