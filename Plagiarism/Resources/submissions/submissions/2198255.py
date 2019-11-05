def replace(pattern, replacement, corpus):
    pattern = " " + pattern + " "
    ln_pattern = len(pattern)
    a = corpus.find(pattern)
    b = corpus[:a] + " " + replacement + " " + corpus[a+ln_pattern:]
    return b