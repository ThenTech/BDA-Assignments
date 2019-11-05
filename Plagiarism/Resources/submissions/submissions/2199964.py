def replace(pattern, replacement, corpus):
    result = corpus.replace(pattern, replacement)
    return result


print(replace("with", "for", "I play with a sentence without words"))
