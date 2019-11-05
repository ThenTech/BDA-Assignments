def substring(string, start_index, number_of_char):
    sub_string = ""
    for i in range(start_index, start_index + number_of_char):
        sub_string += string[i]
    return sub_string

def find_pos(word, sentence):
    for i in range(0, len(sentence)-len(word)+1):
        sub = substring(sentence, i, len(word))
        if word == sub:
            return i
        
def in_string(word, sentence):
    string_pos = find_pos(word, sentence)
    return string_pos != None