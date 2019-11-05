def replace(pattern, replacement, corpus):
    corpus = corpus.split()
    s_a = ''
    for i in corpus:
        if pattern not in i:
            s_a += i + ' '
        else:
            s_a += (replacement + i[len(pattern):])+' '
    return s_a