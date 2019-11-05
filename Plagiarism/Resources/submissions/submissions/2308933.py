def filter_sentence(sentence):
    lower = sentence.lower()
    result = ""
    for ch in lower:
        if ('a' <= ch and ch <= 'z'):
            result += ch
    return result



def is_palindrome(word):
    for i in range(len(word) // 2):
        if (word[i] != word[len(word) - i - 1]):
            return False
    return True



def is_palindrome_sentence(sentence):
    return is_palindrome(filter_sentence(sentence))


