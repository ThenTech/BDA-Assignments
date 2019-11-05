import string





def count_words(string):
    
    def remove_punctuation(string):
        s_without_punct = " "
        for letter in string:
            if letter not in string.punctuation:
                s_without_punct += letter
        return s_without_punct



    def remove_numbers(s_without_punct):
    
        s_without_numb = " "
        for letter in s_without_punct:
            if letter not in string.digits:
                s_without_numb += letter
        return s_without_numb
    
    
    l = s_without_numb.split()
    p = len(l+1)
    return p
    
    



