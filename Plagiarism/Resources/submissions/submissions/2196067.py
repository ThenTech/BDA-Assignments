def replace(pattern, replacement, corpus):
    for x in range(len(corpus)-len(pattern)):
        if corpus[x:len(patten)+x]==pattern:
            corpus = corpus[:x] + replacement + corpus[len(pattern)+x:]
    return corpus