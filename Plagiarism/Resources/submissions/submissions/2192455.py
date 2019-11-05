import string


def is_palindrome_sentence(sentence):
    i = 0
    sentence = "\"\"\"" + sentence + "\"\"\""
    newString = ""
    for letter in sentence:
        if letter not in string.punctuation:
            newString += letter
        else:
            newString += ""

    sentence = ""
    for letter in newString:
        if letter == " ":
            sentence += ""
        else:
            sentence += letter.lower()

    # sentence = newString.replace(" ", "").lower()
    nieuw_woord = ""
    print(sentence)
    while i < len(sentence):
        nieuw_woord = nieuw_woord + sentence[len(sentence) - 1 - i]
        i = i + 1
    if nieuw_woord == sentence:
        return True
    else:
        return False