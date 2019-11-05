def substring(string, start_index, number_of_char):
    sub_string = ""
    for i in range(start_index, number_of_char):
        sub_string += string[i]
    return sub_string

def find_pos(word, sentence):
    current_sentence_index = 0
    first_letter_word = word[0]
    x = 0

    print(sentence, ",", word, ":")
    for letter in sentence:
        if letter == first_letter_word:
            i = current_sentence_index
            while i <= current_sentence_index + len(word) and current_sentence_index + len(word)-1 <= len(sentence):
                if x == len(word):
                    return current_sentence_index
                if sentence[i] == word[x]:
                    x += 1
                    i += 1
                else:
                    break
        x = 0
        current_sentence_index += 1

def in_string(word, sentence):
    string_pos = find_pos(word, sentence)
    
    if string_pos != None:
        return True
    else:
        return False