def replace(pattern, replacement, corpus):
    for i in range(len(corpus)-len(pattern)):
        if pattern == corpus[i:i+len(pattern)]:
            value1 = i
            corpus = corpus[:value1] + replacement + corpus[value1+len(pattern):]
            empty_list = empty_list[1:]
    return corpus