def replace(pattern, replacement, corpus):
    for x in range(len(corpus)-len(pattern)):
        if corpus[x:len(pattern)+x]==pattern:
            corpus = corpus[:x] + replacement + corpus[len(pattern)+x:]
    return corpus