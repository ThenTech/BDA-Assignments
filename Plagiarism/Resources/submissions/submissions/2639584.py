def index(pattern, string):
    i = 0
    while i < len(string) - len(pattern) + 1:
        if string[i:i + len(pattern)] == pattern:
            return i
        i += 1

def replace(pattern, replacement, corpus):
    while pattern in corpus:
        i = index(pattern, corpus)
        corpus = corpus[:i] + replacement + corpus[i + len(pattern):]
    return corpus