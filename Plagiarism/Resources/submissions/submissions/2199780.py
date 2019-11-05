import string

numbers = "0123456789"
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def remove_punctuation(string):
    s_without_punct = ""
    for letter in string:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct



def remove_numbers(s_without_punct):
    s_without_numb = ""
    for letter in s:
        if letter not in string.numbers:
            s_without_numb += letter
    return s_without_numb
    
    
def count_words(s_without_numb):
    l = s_without_numb.split()
    p = len(l)
    
    

    for i in range(p-1):
        word = p[i]
        
        count += 1
    return int(count)



