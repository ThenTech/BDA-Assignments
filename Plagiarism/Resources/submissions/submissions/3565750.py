def replace(pattern, replacement, corpus):
    final_string = ""
    pat_len = len(pattern)
    length = len(corpus)
    for word in range(length):
        if corpus[word:word+pat_len] == pattern:
            final_string += replacement
            word += pat_len
        else:
            final_string += corpus[word]
    return final_string
