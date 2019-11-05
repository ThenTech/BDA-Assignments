def replace(pattern, replacement, corpus):
    for x in range(len(corpus) - len(pattern)):
        if pattern in corpus[x: x + len(pattern)]:
            corpus = corpus[0:x] + replacement + corpus[x + len(pattern):]
    return corpus