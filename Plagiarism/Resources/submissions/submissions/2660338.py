def is_palindrome_sentence(sentence):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    nieuw = ""
    for kar in sentence:
        if kar in alfabet:
            nieuw += kar
    sentence = nieuw
    omgekeerd = ""
    for i in range(len(sentence)):
        omgekeerd += sentence[len(sentence)-i-1]
    return omgekeerd == sentence