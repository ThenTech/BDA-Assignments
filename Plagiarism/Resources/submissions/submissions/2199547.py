def cleanup_spaces(s):
    new_word = ""
    new_sentence = s.split()
    for i in new_sentence:
        new_word += (i + " ")
    return new_word