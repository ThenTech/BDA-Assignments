def replace(pattern, replacement, corpus):
    for i in range(len(corpus)-len(pattern)):
        if corpus[i:i+len(pattern)]== pattern:
            corpus= corpus[:i]+replacement+corpus[i+len(pattern):]
    return corpus