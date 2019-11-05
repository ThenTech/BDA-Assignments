def replace(pattern, replacement, corpus):
    start = 0
    counter = 0
    sentence = ""
    for i in pattern[0]:
        if corpus != "":
            for j in corpus:
                if j != i:
                    counter = counter + 1
                if corpus[counter:counter+len(pattern)] == pattern:
                    end = counter
                    sentence = sentence + corpus[start:end] + replacement
                    start = end + len(pattern)
                    counter = counter + 1
                if counter == len(corpus)-1:
                    sentence = sentence + corpus[start:]
                    return sentence
        return ""