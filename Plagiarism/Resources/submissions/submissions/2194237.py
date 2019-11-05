def is_palindrome_sentence(sentence):
    sentence = sentence.lower()
    overbodig ='0123456789,?;.:/!" "'
    lengthe = len(sentence)
    sentence_new = ""
    for i in range(lengthe-1):
        if sentence[i] not in overbodig:
            sentence_new += sentence[i]
    lengthe_new = len(sentence_new)
    for j in range(lengthe_new-1):
        if sentence_new[j] != sentence_new[lengthe_new -1-j]:
            return False
    return True
