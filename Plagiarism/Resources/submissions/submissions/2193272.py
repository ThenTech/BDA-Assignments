def replace(pattern, replacement, corpus):
    word_list = corpus.split()
    new_string = ''
    for i in word_list:
        if i == pattern:
            new_string += replacement
        else:
            new_string += i
        if i != word_list[len(word_list)-1]:
            new_string += ' '
    return new_string