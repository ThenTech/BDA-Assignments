def is_palindrome_sentence(sentence):
    n = len(sentence)
    x = 1
    if sentence[0] == sentence[n - 1]:
        if sentence[0 + x] == sentence[n - 1 - x]:
            return True
    else:
        return False