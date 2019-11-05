def replace(pattern, replacement, corpus):
    output = ""
    i = 0
    while i < (len(corpus)):
        if corpus[i:i+len(pattern)] == pattern:
            output += replacement
            i += len(pattern)
        else:
            output += corpus[i]
            i += 1
    return output
