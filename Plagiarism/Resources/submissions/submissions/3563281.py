def replace(pattern, replacement, corpus):

    string = ""
    index = 0
    count = 0
    for i in range(len(corpus)):
        if corpus[i:i+len(pattern)] == pattern:
            string += corpus[index:i] + replacement
            index = i + len(replacement) + 1
            count += 1
    if len(string) != len(corpus) - count*len(replacement) + count*len(pattern):
        string += corpus[index:]
    return string