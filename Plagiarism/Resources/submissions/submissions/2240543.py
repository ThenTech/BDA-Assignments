def replace(pattern, replacement, corpus):
    i = 0
    x = ""
    while i < len(corpus):
        slice = corpus[i:i+len(pattern)]
        if slice not in pattern:
            x = x + corpus[i]
            i = i + 1
        else:
            x = x + replacement
            i = i + len(pattern)
    return x