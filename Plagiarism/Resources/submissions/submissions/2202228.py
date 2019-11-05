def cleanup_spaces(s):
    new_word = ""
    new_sentence = s.split()
    for i in range(len(new_sentence)-1):
            new_word += (new_sentence[i] + " ")
    return new_word