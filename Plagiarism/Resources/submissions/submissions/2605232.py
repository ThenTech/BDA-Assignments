def is_palindrome_sentence(sentence):
    sentence_filter = sentence.lower()
    sentence_filter2 = ""
    palindroom = True
    for i in range(len(sentence_filter)):
        if sentence_filter[i] in alfabet:
            sentence_filter2 += sentence_filter[i]
    for i in range(len(sentence_filter1) // 2):
        if sentence_filter1[i] != sentence_filter1[len(sentence_filter)-i-1]:
            return False
        return palindroom
alfabet = "abcdefghijklmnopqrstuvwxyz"
Hoofd
