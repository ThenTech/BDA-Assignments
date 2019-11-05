def is_palindrome_sentence(sentence):
    sentence = sentence.lower()
    sentence_new = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new =""
    for i in range(len(sentence)):
        if sentence[i] in alphabet:
            new += sentence[i]
        else:
            new = new
    lengthe_new = len(new)
    for j in range(lengthe_new-1):
        if sentence_new[j] != sentence_new[lengthe_new -1-j]:
            return False
    return True
    