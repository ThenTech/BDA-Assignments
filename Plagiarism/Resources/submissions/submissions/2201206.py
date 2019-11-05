def cleanup_spaces(string):
    string_len = len(string)
    new_word = ""
    new_sentence = ""
    
    for index in range(string_len):
        if string[index] != " ":
            new_word += string[index]
        elif new_word != "":
                new_sentence += new_word + " "
                new_word = ""
                
    return new_sentence[:len(new_sentence) - 1]