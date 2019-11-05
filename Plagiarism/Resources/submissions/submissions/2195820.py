brol = ''' !"#"$%&'(')*+,-./:;<=>?@]^_`[“\”{|’}~0123456789 '''
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
        return True
    else:
        return False