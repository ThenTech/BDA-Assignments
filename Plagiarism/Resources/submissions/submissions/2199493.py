def replace(pattern, replacement, corpus):
    x = 0
    if pattern not in corpus:
        return " "
    else:
        while x < len(corpus):
            if corpus[x:x+len(pattern)] == pattern:
                corpus = corpus[:x] + replacement + corpus[x+len(replacement)+1:]
            x += 1
        return corpus