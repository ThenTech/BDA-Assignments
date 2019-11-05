def search_start(pattern, string):
    startpos = 0
    max_loop = len(string) - len(pattern)
    for index in range(max_loop):
        if string[index:index+len(pattern)] == pattern:
            startpos = index
    return startpos



def replace(pattern, replacement, corpus):
    if pattern not in corpus:
        return corpus
    while True:
        begin = search_start(pattern, corpus)
        corpus = corpus[:begin] + replacement + corpus[begin+len(pattern):]
        if pattern not in corpus:
            break

    return corpus
print(replace('with','for',"I play with a sentence without words"))