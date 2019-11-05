def is_palindrome_sentence(sentence):
    sentence_filter = sentence.lower()
    sentence_filter2 = ""
    for i in range(len(sentence_filter)):
        if sentence_filter[i] in alfabet:
            sentence_filter2 += sentence_filter[i]
    for j in range(len(sentence_filter2) // 2):
        if sentence_filter2[j] != sentence_filter2[len(sentence_filter2)-j-1]:
            return False
        return True
alfabet = "abcdefghijklmnopqrstuvwxyz"
