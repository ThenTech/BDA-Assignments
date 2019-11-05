def is_palindrome_sentence(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    new_sentence = ""
    reversed_new_sentence = ""

    index = -1

    for char in sentence:
        if char in alphabet:
                new_sentence += char
    new_sentence = new_sentence.lower()

    for char in new_sentence:
        reversed_new_sentence += new_sentence[index]
        index -= 1

    if new_sentence == reversed_new_sentence:
        return True
    else:
        return False