def is_palindrome_sentence(sentence):
    new_sentence = remove_extra_char(sentence)
    
    for index in range(len(new_sentence) // 2):
        if new_sentence[index] != new_sentence[len(new_sentence) - index - 1]:
            return False
    return True
    

def remove_extra_char(string):
    new_string = ""
    for char in string:
        if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            new_string += char.lower()
    return new_string