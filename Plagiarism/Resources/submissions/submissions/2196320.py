def replace(pattern, replacement, corpus):
    lengthe = len(pattern)
    lengthe_2 = len(replacement)
    new =""
    i=0
    while i < (len(corpus)):
        if pattern == corpus[i:i+lengthe]:
            new +=replacement
            i += lengthe
        else:
            new += corpus[i]
            i+=1
    return new