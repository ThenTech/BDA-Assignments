def replace(pattern, replacement, corpus):
    new = ""
    j = 0
    for i in range(len(corpus)):
        if corpus[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                new += replacement
                j = 0
        else:
            for k in range(j+1):
                new += corpus[i-j+k]
            j = 0
    return new