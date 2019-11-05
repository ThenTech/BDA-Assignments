import string

def remove_punctuation(s):
    s_without_punct = ''
    for letter in s:
        if letter not in string.punctuation:
            if letter not in '“”’':
                s_without_punct += letter
        
    return s_without_punct

def remove_space(s):
    s_without_space = ''
    for letter in s:
        if letter != ' ':
            s_without_space += letter
    return s_without_space

def is_palindrome_sentence(sentence):
    sentence = sentence.lower()
    sentence = remove_punctuation(sentence)
    sentence = remove_space(sentence)
    
    x = 0
    
    for i in sentence:
        if i != sentence[(len(sentence)-1) - x]:
            return False
        x = x + 1
    return True