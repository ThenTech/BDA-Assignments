def is_palindrome_sentence(sentence):
    sent = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuwxyz"
    letters = ""
    count = 0
    for i in range(len(sent)):
        if sent[i] in alphabet:
            letters += sent[i]
    for k in range(len(letters)):
        if letters[(len(letters) - 1) - k] == letters[k]:
            count += 1
    if count == len(letters):
        return True
    else:
        return False