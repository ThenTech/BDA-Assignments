brol = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789 "
def cleanup(string):
    zonder_brol = ""
    for letter in string:
        if letter not in brol:
            zonder_brol += letter
    return zonder_brol
def is_palindrome_sentence(sentence):
    sentence = cleanup(sentence)
    reverse = ""
    for letter in range(len(sentence)):
        reverse += sentence[-(letter+1)]
    reverse = reverse.lower()
    sentence = sentence.lower()
    if sentence == reverse:
        print(True)
    else:
        print(False)
is_palindrome_sentence("A Santa dog lived as a devil God at NASA.")