def replace(pattern, replacement, corpus):
    position = 0
    wordFound = False

    for i in range(len(corpus) - len(pattern)):
        word = corpus[i:i+len(pattern)]
        if pattern == word:
            position = i
            wordFound = True
            break

    if wordFound:
        newSentence = corpus[:position] + replacement + corpus[position+len(pattern):]
        return newSentence
