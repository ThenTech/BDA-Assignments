def is_palindrome_sentence(sentence):
    new1sentence = ""
    new2sentence = ""
    sentence = sentence.lower()
    for i in range(len(sentence)):
        if sentence[i] in "abcdefghijklmnopqrstuvwxyz":
            new1sentence += sentence[i]
        if sentence[len(sentence)-i-1] in "abcdefghijklmnopqrstuvwxyz":
            new2sentence += sentence[len(sentence)-i-1]
    print(new1sentence, new2sentence)
    if new2sentence == new1sentence:
        return True
    else:
        return False