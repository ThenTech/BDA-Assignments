def replace(pattern, replacement, corpus):
    i = 0
    while i < len(corpus):
        slice = corpus[i:i+len(pattern)]
        if slice not in pattern:
            print(corpus[i], end="")
            i = i + 1
        else:
            print(replacement, end="")
            i = i + len(pattern)