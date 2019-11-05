def replace(pattern, replacement, corpus):
    i = 0
    while i < len(corpus)-len(pattern)+1:
        pattern_len_corpus = corpus[i: i+len(pattern)] #corpus[Including: Excluding]
        if pattern_len_corpus == pattern:
            corpus = corpus[:i] + replacement + corpus[i + len(replacement) + 1:]
        i += 1
    return corpus