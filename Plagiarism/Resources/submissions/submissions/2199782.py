def remove(w, s):
    s_remove = ''

    for x in s:
        if x not in w:
            s_remove += x
    return s_remove

def replace(pattern, replacement, corpus):
    corpus = corpus.split()
    s_a = ''

    for i in corpus:

        if pattern not in i:
                s_a += i
        else:
           s_a += replacement + remove(pattern, i)

        if i != corpus[len(corpus)-1]:
            s_a += ' '

    return s_a