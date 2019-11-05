def get_only_alpha(s):
    only_alpha = ""
    for letter in s:
        if 'a' <= letter <= 'z' or 'A' <= letter <= 'Z':
            only_alpha += letter
    return only_alpha
    
def is_palindrome_sentence(sentence):
    is_palindrome = True
    sentence = get_only_alpha(sentence)
    sentence = sentence.lower()
    counter = -1
    for i in range(len(sentence) - 1):
        if sentence[i] != sentence[counter]:
            is_palindrome = False
            break
        else:
            counter -= 1
    return is_palindrome