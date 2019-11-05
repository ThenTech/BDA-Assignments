def is_palindrome_sentence(sentence):
    import string
    punc =  string.punctuation
    mirrored = ""
    sentence_ok = ""

    for i in range(0, len(sentence)):
        if sentence[i] not in punc:
            sentence_ok += sentence[i]

    for i in range(0, len(sentence_ok)):
        mirrored = sentence_ok[i] + mirrored

    if mirrored.upper() == sentence_ok.upper():
        return True
    else:
        return False

is_palindrome_sentence("A man, a plan, a canal: Panama")