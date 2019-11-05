def is_palindrome_sentence(sentence):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    sentence.lower()
    test = ""
    for i in range(len(sentence)):
        if sentence[i] in alfabet:
            test += sentence[i]
    if test == test[::-1]:
        return True
    else:
        return False