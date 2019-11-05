def create_sequence(word, start, lenghty):
    new_word = ""
    if start < 0:
        start = len(word)+start
    for i in range(lenghty):
        if start + i >= len(word):
            start -= len(word)
        new_word += word[start+i]
    return new_word