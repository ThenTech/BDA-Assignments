def replace(pattern, replacement, corpus):
    for i in range(len(corpus)-1):
        s = corpus.find(pattern, i)
        if s != -1:
            corpus = corpus[:s] + replacement + corpus[s + len(pattern):]
    return corpus