def substring(string, x, y):
    result = ""
    for i in range(x , x + y ):
        result = result + string[i]

    return result

def find_pos(find_word, sentence):
    end = len(sentence) - len(find_word) - 1
    for i in range(0, end):
        sub = substring(sentence, i, len(find_word))
        if find_word == sub:
            return i

def in_string(check_word, sentence_2):
     return find_pos(check_word, sentence_2) != None