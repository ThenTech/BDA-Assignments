import string




def remove_punctuation(string):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    s_without_punct.sep = " "
    for letter in string:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct



def remove_numbers(s_without_punct):
    numbers = "0123456789"
    s_without_numb.sep = " "
    for letter in s:
        if digit not in string.numbers:
            s_without_numb += letter
    return s_without_numb
    
    
def count_words(s_without_numb):
    l = s_without_numb.split()
    p = len(l)
    return p
    
    



