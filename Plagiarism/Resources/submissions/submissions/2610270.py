def replace(pattern, replacement, corpus):
    copy = corpus
    for i in range(len(corpus)-len(pattern)):
        if corpus[i:i+len(pattern)]== pattern:
            copy = corpus[:i]+replacement+corpus[i+len(pattern):]
    return copy