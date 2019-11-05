def is_palindrome_sentence(sentence):
    sentence_filter = ""
    for i in range(len(sentence)):
        if sentence in alfabet:
            sentence_filter += sentence[i]
    for i in range(sentence_filter // 2):
        if sentence_filter[i] != sentence_filter[len(sentence_filter)-i-1]:
            return False
        return True  
alfabet = "abcdefghijklmnopqrstuvwxyz"
is_palindrome_sentence()