def filter_sentence(sentence):
    lower_sen = sentence.lower()
    new_sentence = ""
    for i in lower_sen:
        if("a" <= i and i <= "z"):
            new_sentence += i

    return new_sentence

def is_palindrome(word):
    for k in range(len(word)):
        if(word[k] != word[len(word) - k - 1]):
            return False
        else:
            return True



def is_palindrome_sentence(sentence):
    return is_palindrome(filter_sentence(sentence))