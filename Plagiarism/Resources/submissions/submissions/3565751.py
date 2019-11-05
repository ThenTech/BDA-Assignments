def replace(pattern, replacement, corpus):
    final_string = ""
    pat_len = len(pattern)
    length = len(corpus)
    maxer = 0
    last = False
    for word in range(length):
        if corpus[word:word+pat_len] == pattern:
            final_string += replacement
            maxer = pat_len
        else:
            if maxer != 0:
                maxer -= 1
                last = True
                continue
            if last:
                final_string += " "
                last = False
            final_string += corpus[word]
    return final_string